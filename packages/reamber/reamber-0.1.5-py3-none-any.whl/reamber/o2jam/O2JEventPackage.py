""" This is the part where OJN stores BPM, Notes, Measure Changes and AutoPlays.

For each level (easy, normal, hard), the number of packages are specified.
So we know how many packages we need to loop through

For each package header, it defines the number of events that will occur after it.

By knowing the amount of events and the location of the note, we can find out the offset

Consider this::

            P E P E E E E P E E P E P E E E E E E E E
    Events  1   4         2     1   8
    Snap      1   1 2 3 4   1 2   1   1 2 3 4 5 6 7 8
    Measure 0   1         1     2   2
    Note      ^       ^       ^   ^               ^

From this, we can tell the offset of the notes by calculating the offset from a BPM List and taking a fraction of
the beat by looking at the snap.

Notice that some snaps have no data in them, these are useful to "pad" these notes into place if they have a complex
snap.

There are more specifications on other data decryption in open2jam_.

.. _open2jam: https://open2jam.wordpress.com/

"""

from __future__ import annotations

import logging
import struct
from collections import deque
from dataclasses import dataclass, field
from typing import List, Union, Dict

from reamber.o2jam.O2JBpm import O2JBpm
from reamber.o2jam.O2JHit import O2JHit
from reamber.o2jam.O2JHold import O2JHold

log = logging.getLogger(__name__)

class O2JConst:

    # These data are required to find out which notes are hits and holds
    HIT_BYTES      : bytes = b'\x00'
    HOLD_HEAD_BYTES: bytes = b'\x02'
    HOLD_TAIL_BYTES: bytes = b'\x03'
    # HIT            : int   = 0  # Not very useful
    # HOLD_HEAD      : int   = 2  # Not very useful
    # HOLD_TAIL      : int   = 3  # Not very useful


class O2JNoteChannel:
    MEASURE_FRACTION: int = 0
    BPM_CHANGE      : int = 1
    COL_1           : int = 2
    COL_2           : int = 3
    COL_3           : int = 4
    COL_4           : int = 5
    COL_5           : int = 6
    COL_6           : int = 7
    COL_7           : int = 8
    COL_RANGE       : range = range(2, 9)
    AUTOPLAY_1      : int = 9
    AUTOPLAY_2      : int = 10
    AUTOPLAY_3      : int = 11
    AUTOPLAY_4      : int = 12
    AUTOPLAY_5      : int = 13
    AUTOPLAY_6      : int = 14
    AUTOPLAY_7      : int = 15
    AUTOPLAY_8      : int = 16
    AUTOPLAY_9      : int = 17
    AUTOPLAY_10     : int = 18
    AUTOPLAY_11     : int = 19
    AUTOPLAY_12     : int = 20
    AUTOPLAY_13     : int = 21
    AUTOPLAY_14     : int = 22
    AUTOPLAY_RANGE  : range = range(9, 23)
    # Is there more?
    # Don't worry about the size of this obj, all of them are static.


@dataclass
class O2JEventMeasureChange:
    """ If the value is 0.75, the size of this measure will be only 75% of a normal measure. """
    # When the channel is 0(fractional measure), the 4 bytes are a float,
    # indicating how much of the measure is actually used,
    # so if the value is 0.75, the size of this measure will be only 75% of a normal measure.
    fracLength: float = 1.0

@dataclass
class O2JEventPackage:
    """ This class facilitates loading of Event Packages. """

    measure: int = 0  # Len 4 (Int)
    channel: int = -1  # Len 2 (Short)
    # There's a Len 2 (Short) indicating how many events there are.
    # Then it's followed by that amount of events.
    events: List[Union[O2JBpm, O2JHit, O2JHold, O2JEventMeasureChange]] =\
        field(default_factory=lambda: [])

    @staticmethod
    def read_event_packages(data: bytes, lvl_pkg_counts: List[int]) -> List[List[O2JEventPackage]]:
        """ Reads all events, this data found after the metadata (300:)

        :param lvl_pkg_counts: The count of pkgs per level
        :param data: All the event data in bytes.
        """

        # Don't think we can reliably get all the offsets of notes, we'll firstly find their measures, then calculate
        # the offsets separately.
        # I have doubts because of bpm changes

        # Because of this, we have to parse LNs in a different wave instead of dynamically like stepmania.

        # Additional variables
        # O2JHit.measure
        # O2JHold.measure
        # O2JHold.tailMeasure

        lvls: List[List[O2JEventPackage]] = []
        data_q = deque(data)

        # Column, Offset
        hold_buffer: Dict[int, O2JHold] = {}

        # For each level, we will read the required amount of packages, then go to the next
        for lvl_pkg_i, lvl_pkg_count in enumerate(lvl_pkg_counts):
            log.debug(f"Loading New Level with {lvl_pkg_count} Packages")
            # noinspection PyTypeChecker
            lvl_pkg: List[O2JEventPackage] = [None] * lvl_pkg_count
            for pkg_i in range(0, lvl_pkg_count):
                if len(data_q) == 0: break
                pkg = O2JEventPackage()
                pkg_data = []
                for i in range(8): pkg_data.append(data_q.popleft())

                pkg.measure = struct.unpack("<i", bytes(pkg_data[0:4]))[0]
                pkg.channel = struct.unpack("<h", bytes(pkg_data[4:6]))[0]
                event_count  = struct.unpack("<h", bytes(pkg_data[6:8]))[0]

                events_data = []
                for i in range(4 * event_count): events_data.append(data_q.popleft())
                events_data = bytes(events_data)

                if pkg.channel in O2JNoteChannel.COL_RANGE:
                    pkg.events += O2JEventPackage.read_events_note(events_data,
                                                                   pkg.channel - 2,  # Package CHN - 2 is column
                                                                   hold_buffer,
                                                                   pkg.measure)
                elif pkg.channel == O2JNoteChannel.BPM_CHANGE:
                    pkg.events += O2JEventPackage.read_events_bpm(events_data,
                                                                  pkg.measure)
                elif pkg.channel == O2JNoteChannel.MEASURE_FRACTION:
                    measure_frac = O2JEventPackage.read_events_measure(events_data)
                    pkg.events.append(O2JEventMeasureChange(measure_frac))
                else:
                    # log.debug(f"{currMeasure} count: {event_count}, chn: {pkg.channel}")
                    pass
                lvl_pkg[pkg_i] = pkg
            lvls.append(lvl_pkg)
        return lvls

    @staticmethod
    def read_events_measure(events_data: bytes) -> float:
        """ Reads the fractional measure data.

        This may not work as intended as there is no ojn files to test this feature.

        :param events_data: The 4 byte data point to unpack.
        :return: Returns a float indicating the fraction of the measure.
        """
        log.warning("Fractional measure isn't confidently implemented, conversion may fail.")
        return struct.unpack("<f", events_data[0:4])[0]

    @staticmethod
    def read_events_bpm(events_data: bytes, curr_measure: float) -> List[O2JBpm]:
        """ Reads the event's bpms.

        Just like the Notes, this can have disabled points where Bpm == 0, that means there's no bpm there.

        This is under the presumption that Bpm == 0 is not supported at all.

        :param events_data: The bytes to unpack.
        :param curr_measure: The current measure, used to calculate the offset later.
        :return: Returns a List of Bpm Points found.
        """
        event_count = int(len(events_data) / 4)
        bpms = []

        for i in range(event_count):
            bpm = struct.unpack("<f", events_data[i * 4:(i + 1) * 4])[0]
            if bpm == 0: continue
            log.debug(f"Appended BPM {bpm} at {curr_measure + i / event_count}")
            bpm = O2JBpm(bpm=bpm, offset=0)
            bpm.measure = curr_measure + i / event_count
            bpms.append(bpm)

        return bpms

    @staticmethod
    def read_events_note(events_data: bytes, column: int,
                         hold_buffer: Dict[int, O2JHold],
                         curr_measure: float) -> List[Union[O2JHit, O2JHold]]:
        """ Reads the event's notes.

        This can have disabled points dictated by the first 2 bytes (see: 'enabled')

        :param events_data: The bytes to unpack.
        :param column: The current column, this can be found in the header.
        :param hold_buffer: The hold buffer, this acts like a static variable to facilitate head and tail matching.
        :param curr_measure: The current measure, used to calculate the offset later.
        :return: Returns a List of Bpm Points found.
        """

        notes = []

        event_count = int(len(events_data) / 4)

        for i in range(event_count):
            enabled = struct.unpack("<h", bytes(events_data[0 + i * 4:2 + i * 4]))[0]
            if enabled == 0: continue

            sub_measure = i / event_count + curr_measure
            volume_pan  = struct.unpack("<s", events_data[2 + i * 4:3 + i * 4])[0]
            volume      = int.from_bytes(volume_pan, 'little') // 16
            pan         = int.from_bytes(volume_pan, 'little') % 16
            note_type   = struct.unpack("<c", events_data[3 + i * 4:4 + i * 4])[0]
            log.debug(f"Event Data: {events_data[0 + i * 4:4 + i * 4]}")

            if note_type == O2JConst.HIT_BYTES:
                hit = O2JHit(volume=volume, pan=pan, offset=0, column=column)
                hit.measure = sub_measure
                notes.append(hit)
                log.debug(f"Appended Note {column} at {sub_measure}")
            elif note_type == O2JConst.HOLD_HEAD_BYTES:
                hold = O2JHold(volume=volume, pan=pan, column=column, length=-1, offset=0)
                hold.measure = sub_measure
                hold_buffer[column] = hold
            elif note_type == O2JConst.HOLD_TAIL_BYTES:
                hold = hold_buffer.pop(column)
                hold.tail_measure = sub_measure
                notes.append(hold)
                log.debug(f"Appended LNote {column} at {sub_measure}, Tail:{hold.tail_measure}")
            else:
                pass
        return notes

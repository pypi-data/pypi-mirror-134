from __future__ import annotations

from reamber.base.Property import item_props
from reamber.base.Note import Note


@item_props()
class HoldTail(Note):
    """ The purpose of this class is to be able to detect the tail as a separate object instead of just Hold

    This class however, is entirely disconnected from Hold, and should only be used for convenience as using the head
    is more natural.
    """

    _props = dict(length=['float', 0.0])
    def __init__(self, offset: float, column: int, length: float, **kwargs):
        super().__init__(offset=offset, column=column, length=length, **kwargs)

@item_props()
class Hold(Note):
    """ A holdable timed object with a specified length.

    We only store the length, the tail offset is calculated.

    We don't directly inherit Hit because the inheritance may be confusing, we'll just subclass Note.
    """

    _props = dict(length=['float', 0.0])

    def __init__(self, offset: float, column: int, length: float, **kwargs):
        super().__init__(offset=offset, column=column, length=length, **kwargs)

    @property
    def tail_offset(self) -> float:
        """ Gets the offset for the tail """
        return self.offset + self.length

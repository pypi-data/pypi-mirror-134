import os
import pytest

from reamber.algorithms.playField import PlayField
from reamber.algorithms.playField.parts import PFDrawBeatLines, PFDrawNotes, PFDrawBpm
from reamber.bms.lists.BMSBpmList import BMSBpmList
from reamber.bms.lists.notes.BMSHitList import BMSHitList
from reamber.bms.lists.notes.BMSHoldList import BMSHoldList
from tests.test.bms.test_fixture import bms_map

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

MAP_READ = os.path.join(THIS_DIR, 'searoad.bml')
MAP_WRITE_EXP = os.path.join(THIS_DIR, 'map_write_expected.bme')
MAP_WRITE = os.path.join(THIS_DIR, 'map_write.bme')


# @profile
def test_type(bms_map):
    assert isinstance(bms_map.hits, BMSHitList)
    assert isinstance(bms_map.holds, BMSHoldList)
    assert isinstance(bms_map.bpms, BMSBpmList)


def test_describe(bms_map):
    bms_map.describe()


def test_meta(bms_map):
    assert bms_map.title == b'searoad tracks =side blue= (LN-Applied)'
    assert bms_map.artist == b'sasakure.UK / obj:moya'
    assert bms_map.version == b'16'


def test_deepcopy(bms_map):
    m = bms_map.deepcopy()
    assert m is not bms_map
    test_meta(m)


def test_stack_mutate(bms_map):
    original = bms_map.hits[0].sample
    bms_map.stack().sample += b'_'
    assert original + b'_' == bms_map.hits[0].sample
    with pytest.raises(TypeError): bms_map.stack().sample += 1


def test_rate(bms_map):
    assert bms_map.stack().offset.min() * 2 == bms_map.rate(0.5).stack().offset.min()


def test_draw(bms_map):
    bms_map.write_file(MAP_WRITE)
    pf = PlayField(bms_map.read_file(MAP_WRITE), padding=50) \
         + PFDrawBeatLines() \
         + PFDrawNotes() \
         + PFDrawBpm()
    pf.export_fold(max_height=2300).save("sm.png")
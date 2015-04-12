from nose.tools import raises
from track.tags import Tags, TAGS
from mp3.reader import MP3Reader
from tests.helpers import GOOD_MP3, BAD_MP3
from tests.helpers import out

WITH_TAGS = MP3Reader(GOOD_MP3)
MISSING_TAGS = MP3Reader(BAD_MP3)


def test_track_tags_load():
    Tags(WITH_TAGS)

def test_track_tags_load_mp3():
    t = Tags(WITH_TAGS)
    assert(t.mp3 is not None)

def test_track_tags_load_mp3_set_properties():
    t = Tags(WITH_TAGS)
    t.set_properties()
    assert(t.artist_name == "Social Distortion")

@raises(AttributeError)
def test_track_tags_raises_not_mp3():
    Tags(object)

def test_track_tags_tag_name_bad():
    t = Tags(WITH_TAGS, tags={"foo": "bar"})
    t.set_properties()
    assert(t.bar is None)

def test_track_tags_missing_tags():
    t = Tags(MISSING_TAGS)
    t.set_properties()
    assert(t.artist_name is None)


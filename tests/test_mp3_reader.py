from nose.tools import raises
from mp3.reader import MP3Reader
from tests.helpers import GOOD_MP3, BAD_MP3

def test_mp3_reader_load():
    MP3Reader(GOOD_MP3)

@raises(IOError)
def test_mp3_reader_load_file_dne():
    MP3Reader("foo")

def test_mp3_reader_load_tagless_mp3():
    # since we know that the BAD_mp3 is tagless
    b = MP3Reader(BAD_MP3)
    assert(len(b._mp3) == 0)

def test_mp3_reader_load_tag_mp3():
    g = MP3Reader(GOOD_MP3)
    assert(len(g._mp3) == 9)

def test_mp3_reader_info_as_property():
    g = MP3Reader(GOOD_MP3)
    assert(g.info == g._mp3.info)

def test_mp3_reader_tags_as_property():
    g = MP3Reader(GOOD_MP3)
    assert(g.tags == g._mp3.tags)

def test_mp3_reader_load_info_length():
    # this is how we would calculate the length of the song
    g = MP3Reader(GOOD_MP3)
    assert(round(g.info.length/60, 1) == 3.8)

def test_mp3_reader_has_tags():
    g = MP3Reader(GOOD_MP3)
    assert(g.has_tags)

def test_mp3_reader_has_no_tags():
    b = MP3Reader(BAD_MP3)
    assert(b.has_tags == False)


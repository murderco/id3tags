from nose.tools import raises
from mp3.reader import MP3Reader
from tests.helpers import GOOD_MP3, BAD_MP3, out

def test_mp3_reader_load():
    MP3Reader(GOOD_MP3)

@raises(IOError)
def test_mp3_reader_load_file_dne():
    MP3Reader("foo")

def test_mp3_reader_load_tagless_mp3():
    # since we know that the BAD_mp3 is tagless
    b = MP3Reader(BAD_MP3)
    assert(len(b.mp3) == 0)

def test_mp3_reader_load_tag_mp3():
    g = MP3Reader(GOOD_MP3)
    assert(len(g.mp3) == 9)

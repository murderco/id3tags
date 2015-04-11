from mutagen.id3 import ID3
from tests.helpers import BAD_MP3, GOOD_MP3, TEST_FILES

def test_can_load_id3():
    ID3()

def test_read_good_mp3_length_9():
    g = ID3(GOOD_MP3)
    assert(len(g) == 9)

def test_read_bad_mp3_length_0():
    b = ID3(BAD_MP3)
    assert(len(b) == 0)


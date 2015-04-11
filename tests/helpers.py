from sys import stderr
from glob import glob

TEST_FILES = glob("tests/*.mp3")
GOOD_MP3 = TEST_FILES[-1]
BAD_MP3 = TEST_FILES[0]

def out(msg):
    stderr.write("{}\n".format(msg))

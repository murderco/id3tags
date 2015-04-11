from mutagen.mp3 import MP3
from logging import debug

class MP3Reader(object):

    def __init__(self, mp3_filename, **kwargs):

        debug("MP3 file is '{}'".format(mp3_filename))
        self.file = mp3_filename

        debug("Loading the MP3 object")
        self.mp3 = MP3(self.file)
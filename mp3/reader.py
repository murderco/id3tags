from mutagen.mp3 import MP3
from logging import debug

class MP3Reader(object):

    def __init__(self, mp3_filename, **kwargs):

        debug("MP3 file is '{}'".format(mp3_filename))
        self.file = mp3_filename

        debug("Loading the MP3 object")
        self._mp3 = MP3(self.file)

    @property
    def info(self):
        """ Info of the file object
        :return: return the mp3 info for the file object
        """
        return self._mp3.info

    @property
    def tags(self):
        """ Tags (or Id3Tags)
        :return: return the id3 tags
        """
        return self._mp3.tags

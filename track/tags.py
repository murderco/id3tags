__author__ = 'Xavier'

# create a global tags, these are TAG NAMES and their corresponding pretty names
TAGS = {
    "TPE1": "artist_name",
    "TALB": "album_name",
    "TIT2": "track_name",
    "TRCK": "track_number",
    "USLT": "lyrics",
    }


class Tags(object):


    def __init__(self, mp3, tags=TAGS):

        self._tags = tags
        self.mp3 = mp3

        # this makes sure that we have an object with tags attributes,
        # if not we want to raise an exception
        if not hasattr(mp3, "tags"):
            raise AttributeError("Unexpected object type {}".format(type(mp3)))


    def set_properties(self):

        for tag_name, new_tag_name in self._tags.items():
            tag_val = None
            if tag_name in self.mp3.tags:
                tag_val = self.mp3.tags[tag_name]
            setattr(self, new_tag_name, tag_val)

    @classmethod
    def run(cls, mp3, tags=TAGS):
        tag = cls(mp3, tags)
        tag.set_properties()
        return tag


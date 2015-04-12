__author__ = 'Xavier'

from mutagen.id3 import *

class Track(object):

    def __init__(self,object):
        self.artist_name = object.getall("TPE1")
        self.album_name = object.getall("TALB")
        self.track_name = object.getall("TIT2")
        self.track_number = object.getall("TRCK")
        self.lyrics = object.getall("USLT")




Killer = Track(ID3("/Users/Xavier/Music/Library/10 Years/Minus the Machine/01 - Minus The Machine.mp3"))
print(Killer.artist_name[0])
print(Killer.album_name[0])
print(Killer.track_name[0])
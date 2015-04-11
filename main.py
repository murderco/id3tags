#!/usr/bin/env python
""" Here is the description of the tool
"""
from playlist_mods import *
from mutagen.id3 import *
from time import *
import os

def SongPath(artist):
    outputList= []
    for items in os.walk("/Users/Xavier/Music/Library/" + artist):
        if items[1] == []:
            for song in items[2]:
                if song.split(".")[1] == "mp3":
                    outputList.append(items[0] + "/" + song)
    return outputList



#items = ["TALB", "USLT", "TBPM", "TCMP", "TCOM", "TCOP", "TENC", "TEXT", "TLEN", "TMED", "TMOO", "TIT2", "TIT3", "TPE1", "TPE2", "TPE3", "TPE4", "TPOS", "TPUB", "TRCK", "TOLY", "TSO2", "TSOA", "TSOC", "TSOP", "TSOT", "TSRC", "TSST", "TLAN"]

<<<<<<< HEAD
#items = ["TALB", "USLT", "TIT2", "TPE1", "TRCK"]

items = ["TPE1", "TALB", "TIT2", "TRCK", "USLT"]
# Playlists pointing to my music library
#songList = playlist("Bad Day.m3u")[0]
"""
# For music files in folder
songList = ["/Users/Xavier/Dropbox/Programming/Python/Trial/02 - Unbreakable.mp3",
            "/Users/Xavier/Dropbox/Programming/Python/Trial/02 Don't Drag Me Down.mp3"]
"""

def info():
    songList = SongPath("")

    fname = open(mode="w",name="Track Info.txt")

    broken = []
    for song in songList:
        audio = ID3(song.split("\n")[0])
        for item in items:
            if audio.getall(item) != [] or item == "TIT2":
                fname.write("{}\n".format(audio.getall(item)))
                if item == "TIT2" and audio.getall(item) == []:
                    broken.append(song)
        audio.save

        fname.write("\n\n\n")

    fname.write("{}\n".format(broken))
    fname.write("{}\n".format(len(broken)))

info()
=======
def clean_id3s():
    for song in songList:
        audio = ID3(song.split("\n")[0])
        for item in items:
            if audio.getall(item) != [] or item == "TLEN":
                print(audio.getall(item))
        audio.save

        print("\nNext Song\n")



if __name__ == "__main__":
    clean_id3s()
>>>>>>> 552f724c01429fb0be74b7d6b5c7040130398ff2

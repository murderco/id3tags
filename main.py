#!/usr/bin/env python
""" Here is the description of the tool
"""
from mutagen.id3 import *
import os

def SongPath(artist):
    outputList= []
    for items in os.walk("/Users/Xavier/Music/Library/" + artist):
        if items[1] == []:
            for song in items[2]:
                if song.split(".")[1] == "mp3":
                    outputList.append(items[0] + "/" + song)
    return outputList


def info():
    items = ["TPE1", "TALB", "TIT2", "TRCK", "USLT"]

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

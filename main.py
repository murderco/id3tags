from playlist_mods import *
from mutagen import ID3

items = ["TALB", "TBPM", "TCMP", "TCOM", "TCOP", "TENC", "TEXT", "TLEN", "TMED", "TMOO", "TIT2", "TIT3", "TPE1", "TPE2", "TPE3", "TPE4", "TPOS", "TPUB", "TRCK", "TOLY", "TSO2", "TSOA", "TSOC", "TSOP", "TSOT", "TSRC", "TSST", "TLAN"]


songList = playlist("Completely Random.m3u")[0]



for song in songList:
    audio = ID3(song.split("\n")[0])
    for item in items:
        if audio.getall(item) != [] or item == "TLEN":
            print(audio.getall(item))
    audio.save

    print("\nNext Song\n")

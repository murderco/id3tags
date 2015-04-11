__author__ = 'Xavier'

from random import *



# Input songlist and make playlist with given name
def make_playlist(songList, playlistName):

    # Make the playlist file
    playlist = open(playlistName, "w")

    for song in songList:
        playlist.write(song)

    playlist.close()



# Makes playlist out of inputted data
def playlist_list(songList, songInfo):

    # Make the playlist output list
    output = list()

    # Should it be written like VLC writes its playlists?

    # Standard first line
    output.append("#EXTM3U\n")

    # add song and info to the playlist file
    for song in range(len(songList)):
        output.append(songInfo[song])
        output.append(songList[song])

    return output



# Input a file and return two list
# (Info and song location)
def playlist(file):

    # All the starting variables needed
    intFile = open(file)
    output1 = list()
    output2 = list()

    # iterate through each line
    for line in intFile.readlines():

        # output2 = All of the info
        if line.split(":")[0] == "#EXTINF":
            output2.append(line)

        # output1 = Location of all the songs
        else:
            if line != "#EXTM3U\n":
                output1.append(line)

    intFile.close()

    return output1, output2



# inputs a playlist file and outputs the length of the playlist
def playlist_length(file):

    # Initialize variables
    intList = playlist(file)[1]
    length = 0

    # iterate through the items containing info
    for string in intList:
        part1 = string.split(":")

        # Only not true on the first line
        if part1[0] == "#EXTINF":
            # Splits it up until the number(length) is alone
            part2 = part1[1].split(",")

            # Adds the number to the total length
            length += int(part2[0])

    return length



# Mixes multiple playlists together
def mixing_playlists(line, ratio, splitter):

    # Initialize all the needed variables
    savedSongs = list()
    savedInfo = list()

    # 'for' loop to separate the specific playlists if necessary
    for item in range(len(line.split(splitter))):
        tempSongs = playlist(line.split(splitter)[item])[0]
        tempInfo = playlist(line.split(splitter)[item])[1]

        # 'for' loops allows input for ratios
        for i in range(int(ratio[item])):
            # the number for the song of a given playlist
            songNumber = randint(0, len(tempSongs)-1)

            # Save the proper song and removes it from list for no repeats
            song = tempSongs[songNumber]
            savedSongs.append(song)
            tempSongs.remove(song)

            # Saves the info for the given song and removes it from list for no repeats
            savedInfo.append(tempInfo[songNumber])
            tempInfo.remove(tempInfo[songNumber])

    # Makes a playlist with the songs and the info of each song
    return playlist_list(savedSongs, savedInfo)
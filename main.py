#!/usr/bin/env python
""" Here is the description of the tool
"""
import os
import logging
from logging.config import fileConfig

from mp3.reader import MP3Reader
from track.tags import Tags

from tests.helpers import GOOD_MP3


def main():
    logging.info("Starting id3 reader/writer")

    logging.info("loading track: {}".format(GOOD_MP3))
    track, tags = load_track(GOOD_MP3)

    for tag_name in tags._tags.values():
        if not hasattr(tags, tag_name): continue
        logging.info("tag {}: {}".format(tag_name, getattr(tags, tag_name)))

def load_track(track_path):
    mp3 = MP3Reader(track_path)
    tags = Tags.run(mp3)
    return mp3, tags

if __name__ == "__main__":
    # create the log file here
    logfile = os.path.join("logs", "id3reader.log")

    # make sure we have the directory made, before starting the logger
    if not os.path.isdir(os.path.dirname(logfile)):
        os.makedirs(os.path.dirname(logfile))

    # set the log level
    loglevel_name = "INFO"

    # config the logger
    fileConfig("logging.conf", defaults={"logfile": logfile, "loglevel": loglevel_name})

    # start the program here
    main()

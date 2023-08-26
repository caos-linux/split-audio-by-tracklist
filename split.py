#!/usr/bin/python3

import sys
import subprocess

import unicodedata
import re

import os

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def main():
    """split a music track into specified sub-tracks by calling ffmpeg from the shell"""

    # check command line for original file and track list file
    if len(sys.argv) != 3:
        print("usage: split <original_track> <track_list>")
        exit(1)

    # record command line args
    original_track = sys.argv[1]
    original_track_ext = os.path.splitext(original_track)[1]
    track_list = sys.argv[2]

    # read each line of the track list and split into start, name
    with open(track_list, "r") as f:
        start=[]
        name=[]
        for line in f:
            # skip comment and empty lines
            if line.startswith("#") or len(line) <= 1:
                continue

            # create command string for a given track
            s,  n = line.strip().split(' ',1)
            start.append(s)
            name.append(slugify(n))

    # create end array        
    end = start.copy()
    end.pop(0)
    end.append("9999:00:00")

    # create a template of the ffmpeg call in advance
    cmd_string = "ffmpeg -hide_banner -i \'{tr}\' -vn -acodec copy -ss {st} -to {en} \'{nm}\'" + original_track_ext

    i = 1
    for st,en,nm in zip(start, end, name):
        command = cmd_string.format(tr=original_track, st=st, en=en, nm='{:02d}'.format(i) + ' - ' + nm)
        print(command)
        subprocess.call(command, shell=True)    
        print("---------------------------------------------------------------------------------------")
        i = i+1
    return None

if __name__ == "__main__":
    main()

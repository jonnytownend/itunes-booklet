from change_system_date import date_added_to_int, set_date
from get_date_added import get_date_added

import os
from datetime import datetime
import xml.etree.ElementTree as elt
import time

from libpytunes import Library

TITLE = '01 Got Ones'
ALBUM = 'Purple Cwtch EP'
ARTIST = 'Ganz'

def reformat_data_added(struct_time):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', struct_time)

def get_tracks(lib_fn):
    lib = Library(lib_fn)
    tracks = []
    for id,song in lib.songs.items():
        if song.location:
            tracks.append(song)
    return tracks

def save_data(tracks, output_fn):
    data = u''
    for track in tracks:
        if track.location:
            if track.name:
                data += track.name + '\t'
            else:
                data += 'NONE\t'
            if track.album:
                data += track.album + '\t'
            else:
                data += 'NONE\t'
            if track.artist:
                data += track.artist + '\t'
            else:
                data += 'NONE\t'
            if track.date_added:
                data += reformat_data_added(track.date_added) + '\n'
            else:
                data += 'NONE\n'

    file = open(output_fn,'w')
    file.write(data.encode('utf8'))
    file.close()

def write_all_metadata(tracks):
    for track in tracks:
        temp = location.replace('.mp3', '_tmp.mp3')
        date_added = time.strftime('%Y-%m-%dT%H:%M:%SZ',track.date_added)
        os.system('ffmpeg -i "{}" -c copy -metadata date_added="{}" "{}"'.format(track_fn, date_added, temp))
        os.system('mv "{}" "{}"'.format(temp, track_fn))

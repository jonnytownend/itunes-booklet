from change_system_date import date_added_to_int, set_date
from get_date_added import get_date_added

import os
from datetime import datetime
import xml.etree.ElementTree as elt
import time

root = elt.parse('lib_copy.xml').getroot()
tracks = root[0][15].findall('dict')

for track in tracks:
    #Go through each track <dict> and compare metadata
    for i in range(len(track)):
        #Pull out relevant metadata for current track
        if track[i].text == 'Date Added':
            date_added = track[i+1].text

    print date_added
    set_date(date_added)
    time.sleep(1)

import xml.etree.ElementTree as elt

def get_date_added(title, artist=None, album=None, libfile='lib_copy.xml'):
    '''
    Searches specified iTunes Library XML file for specified track.

        # Inputs:
        title:      [string]
        artist:     [string]
        album:      [string]
        libfile:    [string]    Path to iTunes Library XML file

        # Returns:
        date_added  [string]
            OR
        None        [None]      Returns None if no track is found in XML

    ## TODO:
    Needs some pre-processing on inputs to ensure any
    unusual characters are handled correctly.
    '''

    root = elt.parse(libfile).getroot()
    tracks = root[0][15].findall('dict') #Array of <dict> objects in XML file, one for each track entry

    for track in tracks:
        #Go through each track <dict> and compare metadata
        for i in range(len(track)):
            #Pull out relevant metadata for current track
            if track[i].text == 'Name':
                title_entry = track[i+1].text
            elif track[i].text == 'Artist':
                artist_entry = track[i+1].text
            elif track[i].text == 'Album':
                album_entry = track[i+1].text

        #Dirty hack if artist and/or album nor present!
        #!! Needs updating !!
        if artist == None:
            artist = artist_entry
        if album == None:
            album = album_entry

        #Compare metadata to identify track.
        #If specified track, pull out the 'Date Added' metadata
        if title_entry == title and artist_entry == artist and album_entry == album:
            for i in range(len(track)):
                if track[i].text == 'Date Added':
                    return track[i+1].text
        else:
            pass
    return None

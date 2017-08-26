import os
from datetime import datetime

def date_added_to_int(date_added):
    '''
    Converts a 'Date Added' date from iTunes XML to an integer
    representation to be used with Unix 'date' command.

        Date Added format example:    2015-05-24T15:28:08Z
        Terminal 'date' format:   {month}{day}{hour}{minute}{year}

    # Inputs:
        date_added  [string]    'Date Added' field from iTunes XML

    # Returns:
        date_int    [string]    An integer representation of the date in
                                string form.
    '''

    dt = datetime.strptime(date_added,'%Y-%m-%dT%H:%M:%SZ')
    date_int = str(dt.month).zfill(2)
    date_int += str(dt.day).zfill(2)
    date_int += str(dt.hour).zfill(2)
    date_int += str(dt.minute).zfill(2)
    date_int += str(dt.year)[2:]

    return date_int

def set_date(date_added):
    '''
    Changes the system date to the specified Date Added from
    iTunes XML
    '''
    date = date_added_to_int(date_added)
    os.system('date '+date)

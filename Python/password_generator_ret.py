#! /usr/bin/python3

'''
detects webpage, fetches the password associated with that webpage. audible tone
if there is no password found
'''

import pandas as pd
import pyperclip, beepy
from re import search
from subprocess import Popen, PIPE 

cmd = "/usr/bin/osascript -e 'tell application \"Safari\"' -e 'get the URL of current tab of window 1' -e 'end tell'"

pipe = Popen(cmd, shell=True, stdout=PIPE).stdout
url = pipe.readlines()
url = str(url)
url = search('https?://([A-Za-z_0-9.-]+).*', url)

my_password_location = []
try:
    url = url.group(1)
    row = pd.read_csv(my_password_location ).loc[[url]] 
    key = row.iloc[0,0]
    pyperclip.copy(key)

except: 
    beepy.beep(3)

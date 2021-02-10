#! /usr/bin/python3
'''
detects current website, generates a random password, and saves the password to a file to be retrieved
'''

import random, pyperclip, beepy
from re import search
from subprocess import Popen, PIPE 

cmd = "/usr/bin/osascript -e 'tell application \"Safari\"' -e 'get the URL of current tab of window 1' -e 'end tell'"

pipe = Popen(cmd, shell=True, stdout=PIPE).stdout
url = pipe.readlines()
url = str(url)
url = search('https?://([A-Za-z_0-9.-]+).*', url)

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[].:;'!@#$%^&*_-+="
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

for _ in range(10):
    all = "".join(random.sample(all, len(all)))

# make sure one of each is present
start = []
start += random.sample(lowercase_letters, 1)
start += random.sample(uppercase_letters, 1)
start += random.sample(digits, 1)
start += random.sample(symbols, 1)
password = ''.join(start)

length = random.randrange(11, 16)
password += "".join(random.sample(all, length))

my_password_location = []

try:
    url = url.group(1)
    pyperclip.copy(password)
    text = url + "," + password + "\n"
    open(my_password_location, "a").write(text)

except: 
    beepy.beep(3)    


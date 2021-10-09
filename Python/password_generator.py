#! /usr/bin/python3

import random, pyperclip, beepy
from re import search
from subprocess import Popen, PIPE 

def get_safari_url():
    cmd = "/usr/bin/osascript -e 'tell application \"Safari\"' -e 'get the URL of current tab of window 1' -e 'end tell'"
    pipe = Popen(cmd, shell=True, stdout=PIPE).stdout
    url = pipe.readlines()
    return url[0]

def random_pass(n=20):
    random_pass = []
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    digits = "0123456789"
    symbols = "(){}[].:;'!@#$%^&*_-+="
    while len(random_pass) <= n:  
        letter = random.sample(upper, 1) + random.sample(lower, 1)
        addnum = letter + random.sample(digits, 1) 
        addsym = addnum + random.sample(symbols, 1)
        random_pass += random.sample(addsym, 4)
    random_pass = random.sample(random_pass, n)
    return "".join(random_pass)
    
web = get_safari_url()
password = random_pass()

out_path # enviroment variable
pyperclip.copy(password)
text = web + "," + password + "\n"

try:
    open(out_path, "a").write(text)
except FileNotFoundError:
    beepy.beep(3)
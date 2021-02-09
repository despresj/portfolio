#! /usr/bin/python3

import random
import pyperclip

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[],.:;'!@#$%^&*_-+="
upper, lower, nums, syms = True, True, True, False
email = ""
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
email = "".join(random.sample(all, length))
email = email + '@gmail.com'

pyperclip.copy(email)
print('Generated Email: "' + email + '" Copied To Clipboard')
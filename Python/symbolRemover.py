#! /usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()
lines = text.split("\n")
for i in range(len(lines)):
    line = lines[i]
    line = str(line)
    lines[i] = line.replace(">", "")

text = '\n'.join(lines)
pyperclip.copy(text)

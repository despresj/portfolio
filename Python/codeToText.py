#! /usr/bin/python3
"""
This will collect all the code in a directory
and create a finder friendly text file.
"""
import os
import shutil

ext = (".py", ".ipynb", ".R", '.Rmd')
folder = ("")
blacklist = ("")

out_path = ""
new_file_with_code = out_path + "Code.txt"


codelist = []

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(ext) and not foldername.startswith(blacklist):
            filename = foldername + "/" + filename 
            
            with open(os.path.join(filename), 'r') as filedata:
                string = filedata.read()
                codelist.append(string)
                codelist.append('#' + '~_'*20)  
          

with open(new_file_with_code, 'w') as filehandle:
    for listitem in codelist:
        filehandle.write('%s\n' % listitem)  
                               
shutil.copyfile(new_file_with_code, out_path + "code.md")
os.remove(new_file_with_code)
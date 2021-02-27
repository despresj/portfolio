#! /usr/bin/python3
"""
This will collect all the code in a directory
and create a finder friendly text file.
"""
import os
import shutil

# select file extensions
ext = (".py", ".ipynb", ".R", '.Rmd')
# Path from which you want to obtian the code
folder = ("")

# any files you want to not include
blacklist = ("")

# directory you would like the combined file
out_path = ""
new_file_with_code = out_path + "Code.txt"


codelist = []

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
      # Iterate through directory selecting file that meets conditions
        if filename.endswith(ext) and not foldername.startswith(blacklist):
            filename = foldername + "/" + filename 
            
            with open(os.path.join(filename), 'r') as filedata:
              # make all code meeting conditions into a list
                string = filedata.read()
                codelist.append(string)
                codelist.append('#' + '~_'*20)  
          
# write this list to a txt file
with open(new_file_with_code, 'w') as filehandle:
    for listitem in codelist:
        filehandle.write('%s\n' % listitem)  
# I prefer markdownfiles because they fit better into my workflow
shutil.copyfile(new_file_with_code, out_path + "code.md")
os.remove(new_file_with_code)

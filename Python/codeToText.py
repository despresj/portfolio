#! /usr/bin/python3
"""
TODO:
test test test
"""

import os
from shutil import copyfile

def combinecode(folder, # Path from which you want to obtian the code
                output_path = os.getcwd(),  
                blacklist = (), # any files you want to not include
                newfile = "codefile.txt",
                mdfile = True, # get make file markdown
                ext = (".py", ".ipynb", ".R", '.Rmd')): # select file extensions
    
    try:
        output_path
    except NameError:
        output_path = folder
    
    codelist = []
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(ext) and not foldername.startswith(blacklist):
                filename = foldername + "/" + filename 
                
                with open(os.path.join(filename), 'r') as filedata:
                    string = filedata.read()
                    codelist.append(string)
                    codelist.append('#' + '_~_|_~_|'*10)  
                    
    with open(newfile, 'w') as filehandle:
        for listitem in codelist:
            filehandle.write('%s\n' % listitem)
    
    if mdfile:
        mdfile = newfile.replace("txt", "md")
        copyfile(newfile, output_path + "/" +  mdfile)
        os.remove(newfile)
        return mdfile
    else:
        copyfile(newfile, output_path + "/" + newfile)
        return newfile

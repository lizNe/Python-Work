#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt.bak"):
        # get the path to the file in the current directory
        # src - source

        src = path.realpath("textfile.txt")
        
        # let's make a backup copy by appending "bak" to the name
        # dst - destination

        # dst = src + ".bak"
        # shutil.copy(src, dst)
        
        # rename the original file
        # os.rename("textfile.txt", "renamedNewfile.txt")
        
        # now put things into a ZIP archive
        # split returns 2 values so thats why root_dir and tail is there

        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        # archive is the name. zip is the file so creating a zip file. Directory you want to place in zip file is root_dir
        # Once created this archive file will be zipped and contain all python files and text files that we are currently using so Ch3 - Exercise


        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip: # newzip is the variable made
            newzip.write("renamedNewfile.txt")
            newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
    main()

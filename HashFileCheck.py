'''
Author: Dylan Fox
Date: 1/11/2023
Verson. 0.0.01

What this program will do:
    Read files in current folder and populate them sort by name into the Hashes.txt 
    Run an MD5 hash of each file and compare it to the MD5 pulled from the site (libgen.is)
    Write output to tell you which files match and which ones don't

!!What you need to do:
    Input the MD5 hash from the website on a new line in the Hashes.txt doc.

'''

import os
import hashlib

CURRENTDIR  = os.path.dirname(os.path.realpath(__file__))
IGNOREFILES = ["HashFileCheck.py", "Hashes.txt", "compare.txt", "test.py"]
HASHFILE = "Hashes.txt"
FILESTOADD = []

# Gets list of filenames to add
for i in os.listdir(CURRENTDIR):
    if i in IGNOREFILES:
        pass
    else:
        FILESTOADD.append(i)

# Opens file to get user inputed hashes
SiteHash = []
f = open(HASHFILE)
for line in f:
    SiteHash.append(line)
f.close()
SiteHash = list(map(lambda s: s.strip(), SiteHash)) # Removes newline char from list elements

# Opens and appends filenames to end of each line
f = open('compare.txt', 'w')
for i in range(len(FILESTOADD)-1):
    f.write(SiteHash[i] + ":" + FILESTOADD[i] + '\n')

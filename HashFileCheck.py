'''
Author: Dylan Fox
Date: 1/11/2023
Verson. 0.1.0

What this program will do:
    Read files in current folder and populate them sort by name into the MD5Hashes.txt 
    Run an MD5 hash of each file and compare it to the MD5 pulled from the site (libgen.is)
    Write output to tell you which files match and which ones don't

!!What you need to do:
    Input the MD5 hash from the website on a new line in the MD5Hashes.txt doc.

'''

import os # Used for finding files folder
import hashlib # Used to hash files that will be compared

# Console colors
class bcolors:
    OKGREEN = '\033[32m'
    FAIL = '\033[31m'
    ENDC = '\033[m'



CURRENTDIR  = os.path.dirname(os.path.realpath(__file__))
os.chdir(CURRENTDIR)
# Required program files
IGNOREFILES = ["HashFileCheck.py", "MD5Hashes.txt", "RUN.bat"]
HASHFILE = "MD5Hashes.txt"



# Gets list of filenames in programs dir
FilesNames = []
for i in os.listdir(CURRENTDIR):
    if i in IGNOREFILES:
        pass
    else:
        FilesNames.append(i)



# Opens file to get user inputted hashes
SiteHashes = []
f = open(HASHFILE)
for line in f:
    SiteHashes.append(line)
f.close()
SiteHashes = list(map(lambda s: s.strip(), SiteHashes)) # Removes newline char from list elements



# Opens files in the FileNames list, reads content, generate MD5 hash
FileHashes = []
for i in range(len(FilesNames)):
    f = open(FilesNames[i],'rb')
    m = hashlib.md5()
    while True:
        ## Don't read the entire file at once...
        data = f.read(10240)
        if len(data) == 0:
            break
        m.update(data)
    FileHashes.append(m.hexdigest())


# !Brute force! Compares each hash generated in previous func to user inputted hashes. If found, prints results and adds to GoodFiles list
GoodFiles = []
for i in range(len(FileHashes)):
    for j in range(len(FileHashes)):
        if SiteHashes[i] in FileHashes[j]:
            print(bcolors.OKGREEN + "GOOD" + bcolors.ENDC + ": " + FilesNames[j])
            GoodFiles.append(FilesNames[j])

# !Brute force! Iterates through to see which file is in FileNames and not GoodFiles to determine which, if any files failed the check
for i in range(len(FilesNames)):
    if FilesNames[i] in GoodFiles:
        pass
    else:
        print(bcolors.FAIL + "FAIL" + bcolors.ENDC + ": " + FilesNames[i])
print("\nStats of processed Files:")
print("Number of " + bcolors.OKGREEN + "GOOD" + bcolors.ENDC + " files: " + str(len(GoodFiles)))
print("Number of " + bcolors.FAIL+ "BAD" + bcolors.ENDC + " files: " + str(len(FilesNames) - len(GoodFiles)))



# Keeps script from closing when ran from console
print("Press any key to exit.")
input()

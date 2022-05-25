import feedparser
from datetime import datetime
import time
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.dat")

latest = 0
raw_atom = feedparser.parse("https://github.com/paritytech/polkadot/releases.atom")

#Time variables
now = datetime.now()
d = now.strftime("%d/%m/%Y %H:%M:%S")

#Parse the .atom
entries = raw_atom['entries']
link = entries[latest]['link']
version = entries[latest]['title']

#Split on limitor
versionNumber = version.split(":")

if "-h" in sys.argv:
    sys.stdout.write("""Twitter_Alert.py \n
    Useage: \n
    -h      Shows this message \n
    -i      Initalizes Data file \n
    """)
    quit()

#Write current version to file to Initalize the data
if "-i" in sys.argv:
    f = open(DATA_FILE, "w")
    f.write(versionNumber[0])
    f.close()

#Read data file
f = open(DATA_FILE, "r")

#Checks if current version number is stored in the data file
if versionNumber[0] in f.read():
    sys.stdout.write("Checked: " + d + " " + time.tzname[0] + "\n")
    f.close()
    quit()

#A new version has been released
else:
    sys.stdout.write("[!]New Release Detected: " + versionNumber[0] + "\n" )

    f = open(DATA_FILE, "w")

    #Check if version is a release canidate
    if 'rc' in versionNumber:
        print("Release Candidate: " + versionNumber[0] + "has been published" )
        f.write(versionNumber[0])

    #Version is a release
    else:
        print("[!] New Release: " + versionNumber[0] + "\n" + link )
        f.write(versionNumber[0])

#Close the data file once updated
f.close()
quit()

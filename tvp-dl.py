#!/usr/bin/python
# tvp-dl is used to download .wmv files from tvp.pl
# good idea if you're not about to play with silverlight!

import os, sys, urllib, json, re

def quit(mess=""):
    print ("Something is wrong... " + mess)
    sys.exit()

if len(sys.argv) < 2:
    print("Welcome to tvpw-dl!")
    print("\tUsage: %s url" % sys.argv[0])
    print("\tExample: %s http://www.tvp.pl/warszawa/magazyny/campusnews/wideo/31102013/12878238" % sys.argv[0])
    sys.exit()

print ("Let's start!")

try:
    sock = urllib.urlopen(sys.argv[1])
    html = sock.read()
except:
    quit("tvp.pl is not working")
else:
    sock.close()

k = re.compile('object_id:\'[0-9]+\'').search(html)

if k.group() == None:
    quit("tvp-dl is outdated or url is not correct")
    
num = k.group().split('\'')[1]

try:
    sock = urllib.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=%s' % num)
    html = sock.read()
except:
    quit("tvp.pl is not working")
else:
    sock.close()

try:
    d = json.loads(html)
except:
    quit("can't load json...")

if not d['file_name']:
    quit("json does not contain video's url")

print ("Downloading...")

# yes, I know, it's not the best way, but wget is cool
# if you don't like it, fork it and commit new version!
os.system("wget %s" % d['video_url'])

print ("Done! Saved to %s" % d['file_name'])


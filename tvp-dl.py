#!/usr/bin/python
# tvp-dl is used to download .wmv files from tvp.pl
# good idea if you're not about to play with silverlight!

import os, sys, urllib, json, re

if len(sys.argv) < 2:
    print("Welcome to tvpw-dl!")
    print("\tUsage: %s url" % sys.argv[0])
    print("\tExample: %s http://www.tvp.pl/warszawa/magazyny/campusnews/wideo/31102013/12878238" % sys.argv[0])
    sys.exit()

print ("Let's start!")

try:
    sock = urllib.urlopen(sys.argv[1])
    html = sock.read()
    sock.close()
except:
    print ("Something is wrong... tvp.pl is not working!")
    sys.exit()

p = re.compile('object_id:\'[0-9]+\'')
k = p.search(html)

if k.group() == None:
    print ("Something is wrong... with tvp.pl! (or you)")
    sys.exit()
    
num = k.group().split('\'')[1]

try:
    sock = urllib.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=%s' % num)
    html = sock.read()
    sock.close()

    d = json.loads(html)
except:
    print ("Something is wrong... with tvp.pl!")
    sys.exit()

if not d['file_name']:
    print ("Something is wrong... with tvp.pl!")
    sys.exit()

print ("Downloading...")

# yes, I know, it's not the best way, but wget is very good!
os.system("wget %s" % d['video_url'])

print ("Done! Saved to %s" % d['file_name'])


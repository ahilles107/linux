#!/usr/bin/python
# tvp-dl is used to download .wmv files from tvp.pl
# good idea if you're not about to play with silverlight!

import os, sys, urllib, json, re

def quit(mess):
    print (mess)
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
    quit ("Something is wrong... tvp.pl is not working!")
else:
    sock.close()

p = re.compile('object_id:\'[0-9]+\'')
k = p.search(html)

if k.group() == None:
    quit ("Something is wrong... with tvp.pl! (or you)")
    
num = k.group().split('\'')[1]

try:
    sock = urllib.urlopen('http://www.tvp.pl/pub/stat/videofileinfo?video_id=%s' % num)
    html = sock.read()
except:
    quit ("Something is wrong... with tvp.pl!")
else:
    sock.close()

try:
    d = json.loads(html)
except:
    quit ("Something is wrong... with tvp.pl!")

if not d['file_name']:
    quit ("Something is wrong... with tvp.pl!")

print ("Downloading...")

# yes, I know, it's not the best way, but wget is very good!
os.system("wget %s" % d['video_url'])

print ("Done! Saved to %s" % d['file_name'])


#!/usr/bin/python
# tvp-dl is used to download .wmv files from tvp.pl
# good idea if you're not about to play with silverlight!
#
#This is free and unencumbered software released into the public domain.
#
#Anyone is free to copy, modify, publish, use, compile, sell, or
#distribute this software, either in source code form or as a compiled
#binary, for any purpose, commercial or non-commercial, and by any
#means.
#
#In jurisdictions that recognize copyright laws, the author or authors
#of this software dedicate any and all copyright interest in the
#software to the public domain. We make this dedication for the benefit
#of the public at large and to the detriment of our heirs and
#successors. We intend this dedication to be an overt act of
#relinquishment in perpetuity of all present and future rights to this
#software under copyright law.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#
#For more information, please refer to <http://unlicense.org/>

import os, sys, urllib, json, re

def quit(mess=""):
    print ("Something is wrong... " + mess)
    sys.exit()

if len(sys.argv) < 2:
    print("Welcome to tvp-dl!")
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


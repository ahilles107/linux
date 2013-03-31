#! /usr/bin/python

import sqlite3
import sys

if len(sys.argv) == 1:
	print ("Usage: %s yt_id" % sys.argv[0])
	sys.exit()

conn = sqlite3.connect('baza.db')
c = conn.cursor()
c.execute("INSERT INTO yt VALUES ('%s')" % sys.argv[1])
conn.commit()
conn.close()


#! /usr/bin/python

import sqlite3
import sys

conn = None
url = ""
try:
	while not (url == "q"):
		url = raw_input(" > ")
		if not (url == "q"):
			conn = sqlite3.connect('baza.db')
			c = conn.cursor()
			c.execute("INSERT INTO yt VALUES ('%s')" % url)
			conn.commit()
			conn.close()
except:
	pass

print ""
if (not conn == None):
	conn.close()


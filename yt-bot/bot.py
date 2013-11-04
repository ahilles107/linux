#! /usr/bin/python

import sqlite3
import time
import os

while (True):
	conn = sqlite3.connect('baza.db')
	c = conn.cursor()
	c.execute("SELECT * FROM yt")
	url = c.fetchone()
	if not url == None:
		c.execute("DELETE FROM yt WHERE url = '%s'" % (url))
		conn.commit()
		os.system('yt.sh "%s"' % url)
	conn.close()
	time.sleep(2)


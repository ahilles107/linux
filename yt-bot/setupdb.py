#! /usr/bin/python

import sqlite3
import sys

conn = sqlite3.connect('baza.db')
c = conn.cursor()
c.execute("CREATE TABLE yt (url text)")
conn.commit()
conn.close()


#!/usr/bin/python
#
# script's executing shutdown when battery is chardged in > 95%
# usage // add script to root's cron

import os

p = int(os.popen('/usr/bin/acpi -b').read().split(" ")[3].split("%")[0])
if p > 95:
	os.system("crontab -r")
	os.system("shutdown -h 0")


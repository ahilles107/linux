# power management
# author: maciej plonski / mplonski / sokoli.pl
#
# LINUX ONLY!
#
# script is asking you about every loaded kernel module
# if you choose 1, 2 or 3 it's adding module (you've been
# asked about) to the list
# in the end it creats 3 files (battery1.sh, battery2.sh,
# battery3.sh) with commands to unload chosen modules
#
# IMPORTANT! run script and generated files as root!
#
# TODO:
# - remove generating .sh files and create turnon and turnoff
# - add manual
# - have fun

import commands
import subprocess as sub
import sys
import re

def manual():
	print "manual"

def modinfo(name):
	od = commands.getstatusoutput('/sbin/modinfo ' + name + ' | grep depends')[1]
	od2 = re.sub(r'\s', '', od).split(":")[1]
	des = commands.getstatusoutput('/sbin/modinfo ' + name + ' | grep description')[1]
	des2 = re.sub('description:', '', des)
	if len(od2) == 0:
		return [des2, None]
	else:
		return [des2, od2]

def ischeck(i, c):
	for k in c:
		if i == k:
			return 0
	if i == "":
		return 0
	return 1

def dolacz(i, c):
	global osz1
	global osz2
	global osz3

	if(i == 1):
		if ischeck(c, osz1) == 0:
			osz1.append(c)
	elif(i == 2):
		if ischeck(c, osz2) == 0:
			osz2.append(c)
	elif(i == 3):
		if ischeck(c, osz3) == 0:
			osz3.append(c)
	else:
		print 'blad'

def askformodules():

	global osz1
	global osz2
	global osz3

	print " For each module please select:\n  - 0 - do nothing\n  - 1,2,3 - add to battery1/2/3.sh"
	output = commands.getstatusoutput('lsmod')[1]
	for i in range(1, len(output.split("\n"))):
		mod = output.split("\n")[i].split(" ")[0]
		desc, deps = modinfo(mod)
		if deps == None:
			deps = ""
		odp = int(raw_input("\n\nModule: " + mod + "\n Description: " + desc + "\n Depends: " + deps + "\n Select 0,1,2,3 >> "))
		if (odp > 0):
			dolacz(odp, mod)
			if (deps != ""):
				for k in deps.split(","):
					dolacz(odp, k)

	print "selected modules: "
	print ("\n1) ")
	print osz1

	posz1 = open('battery1.sh', 'w')
	for k in osz1:
		posz1.write('modprobe -r ' + k + "\n")
	posz1.close()

	print "\n2) "
	print osz2

	posz2 = open('battery2.sh', 'w')
	for k in osz2:
		posz2.write('modprobe -r ' + k + "\n")
	posz2.close()

	print "\n3) "
	print osz3

	posz3 = open('battery3.sh', 'w')
	for k in osz3:
		posz3.write('modprobe -r ' + k + "\n")
	posz3.close()

def turnoff(tryb):
	print "TODO"

def turnon():
	print "TODO"

osz1 = []
osz2 = []
osz3 = []

if len(sys.argv) > 1:
	if sys.argv[1] == '--setup':
		askformodules()
	elif sys.argv[1] == '--turnoff':
		try:
			if int(sys.argv[2]) > 0:
				turnoff(sys.argv[3])
			else:
				manual()
		except:
			manual()
	elif sys.argv[1] == '--turnon':
		turnon()
	else:
		manual()

else:
	manual()

#!/usr/bin/python
# subtitles tester by mplonski // sokoli.pl
# works on subtitles only in following formats:
# [sec][sec] sth
# {sec}{sec} sth
# LINUX only!

import os, sys

# def checking provided file
def napitest(repair):
	# getting lines from file
	text = open(txtfile)
	lines = text.readlines()
	text.close()

	# removing empty lines
	# warning! empty files are NOT being removed from the file if errors are not found or --repair is not set
	lines = [l for l in lines if l.strip()]

	# do it!
	try:
		# detects subtitle's file's format
		znak = lines[0][0]
		if znak == "[":
			znak2 = "]"
		elif znak == "{":
			znak2 = "}"
		else:
			return ["invalid file format (run with argument --help)", 0]

		# this is where the fun starts!
		wiersz = lines[0]
		pierw = int(wiersz.split(znak2)[1].split(znak)[1])
		err = "errors in lines: "

		# i = 1 (error found), i = 0 (no errors found)
		i = 0

		# checking every line of file
		for num in range(1, len(lines)):
			wiersz = lines[num]
			nast = int(wiersz.split(znak2)[0].split(znak)[1])
			if nast < pierw: # is next subtitle showing up at earlier time than the previous one hides?
				err += (str(num) + " ")
				i = 1
				if (repair == 1):
					if (repair_max == 1):
						lines[num] = znak + str(pierw+1) + znak2 + znak + wiersz.split(znak2)[1].split(znak)[1] + znak2 + wiersz.split(znak2, 2)[2]
					elif (repair_min == 1):
						cache = lines[num-1]
						lines[num-1] = znak + cache.split(znak2)[0].split(znak)[1] + znak2 + znak + str(nast-1)  + znak2 + cache.split(znak2, 2)[2]
					else:
						cache = lines[num-1]
						lines[num-1] = znak + cache.split(znak2)[0].split(znak)[1] + znak2 + znak + str(int((pierw+nast)/2)) + znak2 + cache.split(znak2, 2)[2]
						lines[num] = znak + str(int((pierw+nast)/2)+1) + znak2 + znak + wiersz.split(znak2)[1].split(znak)[1] + znak2 + wiersz.split(znak2, 2)[2]
			pierw = int(wiersz.split(znak2)[1].split(znak)[1])
		if (i == 0):
			if (ok == 0):
				return ["no errors found", 0]
			else:
				return None
		else:
			if (repair == 1):
				if(backup == 0):
					os.system('cp "./' + txtfile + '" "./' + txtfile + '_old"')
				new = open(txtfile, "w")
				new.writelines(lines)
				new.close()
				return [err, 1]
			return [err, 0]
	except:
		return ["something wrong with the file", 0]

# def checks all files matching *.txt* in current directory
def checkdir(repair):
	files = os.listdir(os.curdir)
	il = 0
	repaired = 0
	global txtfile
	for txtfile in files:
		if ".txt" in txtfile:
			il += 1
			tmp = napitest(repair)
			if tmp != None:
				print ("\n" + txtfile + " >> " + tmp[0])
				if tmp[1] == 1:
					repaired = 1
	print("\ntested " + str(il) + " file(s)")
	return repaired

# just some variables
help2 = 0
ok = 1
repair = 0
repair_min = 0
repair_max = 0
backup = 0
txtfile = ""

#analysis of arguments
if(len(sys.argv) > 1):
	for i in range(1, len(sys.argv)):
		if (sys.argv[i] == '--all'):
			ok = 0
		elif (sys.argv[i] == '--help'):
			help2 = 1
		elif (sys.argv[i] == '--nobackup'):
			backup = 1
		elif (sys.argv[i] == '--repair'):
			if(len(sys.argv) > i+1):
				if(sys.argv[i+1] == 'min'):
					repair_min = 1
					i += 1
				elif(sys.argv[i+1] == 'max'):
					repair_max = 1
					i += 1
			repair = 1

# --help ?
if (help2 == 1):
	print "testsub manual\n\ntestsub is small python/linux script testing subtitles -- it tests whether every subtitle has show-time later than previous one\n\nmagic by mplonski // sokoli.pl\nlicence: GNU GPL\n\nusage:\n - to test subtitle (displays only errors): testsub.py\n - to test subtitles and to display information about all files (also the good ones): testsub.py --all\n - to display this manual: testsub.py --help\n\nRepair-mode usage:\n - to change wrong times to arithmetic mean of invalid times: testsub.py --repair\n - to change wrong times to earlier time: testsub.py --repair min\n - to change wrong times to later time: testsub.py --repair max"
else:
	# script checks files again when at least one file has been repaired
	if checkdir(repair) == 1:
		print ("\n\n after repair:\n")
		checkdir(0)


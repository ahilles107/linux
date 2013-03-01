#!/usr/bin/python
# subtitles tester by mplonski // sokoli.pl
# works on subtitles only in following formats:
# [sec][sec] sth
# {sec}{sec} sth
# LINUX only!

from os import listdir,curdir,system
from re import search
from sys import argv

class testsub:
	def __init__(self, argv):
		self.znak = ""
		self.znak2 = ""
		self.help2 = 0
		self.ok = 1
		self.repair = 0
		self.repair_min = 0
		self.repair_max = 0
		self.backup = 0

		for i in range(1, len(argv)):
			if (argv[i] == '--all'):
				self.ok = 0
			elif (argv[i] == '--help'):
				self.help2 = 1
			elif (argv[i] == '--nobackup'):
				self.backup = 1
			elif (argv[i] == '--repair'):
				if(len(argv) > i+1):
					if(argv[i+1] == 'min'):
						self.repair_min = 1
						self.i += 1
					elif(argv[i+1] == 'max'):
						repair_max = 1
						self.i += 1
				self.repair = 1


	def gethelp(self):
		return "testsub manual\n\ntestsub is small python/linux script testing subtitles -- it tests whether every subtitle has show-time later than previous one\n\nmagic by mplonski // sokoli.pl\nlicence: GNU GPL\n\nusage:\n - to test subtitle (displays only errors): testsub.py\n - to test subtitles and to display information about all files (also the good ones): testsub.py --all\n - to display this manual: testsub.py --help\n\nRepair-mode usage:\n - to change wrong times to arithmetic mean of invalid times: testsub.py --repair\n - to change wrong times to earlier time: testsub.py --repair min\n - to change wrong times to later time: testsub.py --repair max"

	# creates line from t1, t2 and txt
	def getline(self, t1, t2, txt):
		return (self.znak + str(t1) + self.znak2 + self.znak + str(t2) + self.znak2 + txt)

	# gets times of showing and hiding `w`
	def gettime(self, w):
		return [int(w.split(self.znak2)[0].split(self.znak)[1]), int(w.split(self.znak2)[1].split(self.znak)[1])]

	# def checking provided file
	def napitest(self, txtfile, repair):
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
			self.znak = lines[0][0]
			if self.znak == "[":
				self.znak2 = "]"
			elif self.znak == "{":
				self.znak2 = "}"
			else:
				return ["invalid file format (run with argument --help)", 0]
	
			# this is where the fun starts!
			wiersz = lines[0]
			pierw = int(wiersz.split(self.znak2)[1].split(self.znak)[1])
			err = "errors in lines: "
	
			# i = 1 (error found), i = 0 (no errors found)
			i = 0
	
			# checking every line of file
			for num in range(1, len(lines)):
				wiersz = lines[num]
				nast = self.gettime(wiersz)[0]
				if nast < pierw: # is next subtitle showing up at earlier time than the previous one hides?
					err += (str(num) + " ")
					i = 1
					if (self.repair == 1):
						if (self.repair_max == 1):
							lines[num] = self.getline(pierw+1, self.gettime(wiersz)[1], wiersz.split(znak2, 2)[2])
						elif (self.repair_min == 1):
							cache = lines[num-1]
							lines[num-1] = self.getline(self.gettime(cache)[0], nast-1, cache.split(znak2, 2)[2])
						else:
							cache = lines[num-1]
							nt = int(pierw+nast)/2
							if not((nt > self.gettime(cache)[0]) and (nt < self.gettime(wiersz)[1]) and (nt - self.gettime(cache)[0] > 2) and (self.gettime(wiersz)[1] - nt > 2)):
								nt = (self.gettime(cache)[0] + self.gettime(wiersz)[1])/2
							lines[num-1] = self.getline(self.gettime(cache)[0], nt, cache.split(self.znak2, 2)[2])
							lines[num] = self.getline(nt+1, self.gettime(wiersz)[1], wiersz.split(self.znak2, 2)[2])
				pierw = self.gettime(wiersz)[1]
			if (i == 0):
				if (self.ok == 0):
					return ["no errors found", 0]
				else:
					return None
			else:
				if (self.repair == 1):
					if(self.backup == 0):
						system('cp "./' + txtfile + '" "./' + txtfile + '_old"')
					new = open(txtfile, "w")
					new.writelines(lines)
					new.close()
					return [err, 1]
				return [err, 0]
		except:
			return ["something wrong with the file (or some bug in this script)", 0]
	
	# def checks all files matching *.txt* in current directory
	def checkdir(self, repair):
		files = listdir(curdir)
		il = 0
		repaired = 0
		for txtfile in files:
			if search('.txt$', txtfile) != None:
				il += 1
				tmp = self.napitest(txtfile, repair)
				if tmp != None:
					print ("\n" + txtfile + " >> " + tmp[0])
					if tmp[1] == 1:
						repaired = 1
		print("\ntested " + str(il) + " file(s)")
		return repaired

	def work(self):
		if self.help2 == 1:
			print self.gethelp()
		else:
			if self.checkdir(self.repair) == 1:
				print ("\n\n after repair:\n")
				self.checkdir(0)

tester = testsub(argv)
tester.work()


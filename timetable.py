import numpy
from tabulate import tabulate
import platform
import sys
import os

'''
weeks: indices [0, 30) --> week no. [1, 30]
days: indices [0, 5) --> {Monday, Tuesday, Wednesday, Thursday, Friday}
times: indices [0, 9) --> {9 am, 10 am, 11 am, 12 pm, 1 pm, 2 pm, 3 pm, 4 pm, 5 pm} 
'''
class Class:
	name = None
	lect = None
	room = None
	def __init__(self, name, lect, room):
		self.name = name
		self.lect = lect
		self.room = room
	
	def getProp(self):
		return (self.name, self.lect, self.room)

class Manager:
	FREE = Class("", "n/a", "n/a")
	classID = None
	classes = None
	TABLE = None
	DAY = {"Mon": 0, "Tue": 1, "Wed": 2, "Thur": 3, "Fri": 4}
	PERIOD = {"9 am": 0, "10 am": 1, "11 am": 2, "12 pm": 3, "1 pm": 4, "2 pm": 5, "3 pm": 6, "4 pm": 7, "5 pm": 8}
	def clearAll(self):
		self.classID = {"FREE": 0}
		self.classes = [self.FREE]
		self.TABLE = numpy.zeros((30, 5, 9), dtype = int)

	def addClass(self, name, lect, room):
		c = Class(name, lect, room)
		self.classes.append(c)
		self.classID[name] = len(self.classes) - 1
	
	def delClass(self, name):
		self.classes[self.classID[name]].name = ""
		self.classID[name] = 0

	def listClasses(self):
		print("Classes: ")
		for co in self.classes[1:]:
			c = co.getProp()
			if(c[0] != ""): print("{}; {}; {}".format(c[0], c[1], c[2]))
			
	def setClass(self, name, week, day, period):
		if(name in self.classID): 
			if(type(week) !=  int):
				for w in self.wr(week[0], week[1]): 
					if(self.TABLE[w - 1, self.DAY[day], self.PERIOD[period]] != 0): print("Overwriting something.")
					self.TABLE[w - 1, self.DAY[day], self.PERIOD[period]] = self.classID[name]
			else:
				self.TABLE[week - 1, self.DAY[day], self.PERIOD[period]] = self.classID[name]
		else: print("Class name not recognised.")
		
	def showTable(self, week, showList = False):
		WEEK = numpy.transpose(self.TABLE[week - 1])
		OUT = [["9 am"], ["10 am"], ["11 am"], ["12 pm"], ["1 pm"], ["2 pm"], ["3 pm"], ["4 pm"], ["5 pm"]]
		for i in range(len(OUT)):
			for p in WEEK[i]:
				OUT[i].append(self.classes[p].name)
		OUT = numpy.array(OUT)
		form = tabulate(OUT, headers = ["Time", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], tablefmt = "grid")
		print(form)
		if(showList): self.listClasses()
	
	def wr(self, a, b):
		l = range(a, b+1)
		return l
		
	def save(self, name):
		npclasses = []
		for c in self.classes[1:]:
			npclasses.append(c.getProp())
		npclasses = numpy.array(npclasses)
		numpy.save("{}_table.npy".format(name), self.TABLE)
		numpy.save("{}_classes.npy".format(name), npclasses)
		
		
	def load(self, name):
		npclasses = numpy.load("{}_classes.npy".format(name))
		for tup in npclasses:
			self.addClass(tup[0], tup[1], tup[2])
		self.TABLE = numpy.load("{}_table.npy".format(name))

		
	
manager = Manager()
	
manager.clearAll()

print("Welcome to the Offical Matthew Smith Timetable Manager. Current instructions are in the README.md file on the GitHub repository.")

while(True):
	user = input(">> ")
	if(user == "exit()"): exit()
	elif(user == "cls"): 
		if(platform.system() == "Windows"): os.system("cls")
		elif(platform.system() == "Linux"): os.system("clear")
		elif(platform.system() == "Darwin"): os.sytem("clear")
		else:
			print("Cannot clear screen. System is unknown.")
	else:
		try:
			exec("manager." + user)
		except:
			print("Failed. Check command and arguments.")
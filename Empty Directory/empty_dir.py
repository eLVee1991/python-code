#!/usr/bin/env python

import os
import glob
import subprocess

# hashes to be used in most print statements to sort te code in the terminal.
singlehash = '''
######################################################################
'''
doublehash = '''
######################################################################
######################################################################
'''

# a list that needs to be callable globally
directory = ("/media/elvee/FILES/LINUX/Klaas/")
directory2 = ("/media/elvee/FILES/Klaas/")
directory3 = ("/media/FILES/Klaas/")
directory4 = ("/media/FILES/LINUX/Klaas/")

list_of_all_dir =[
"directory = /media/elvee/FILES/Klaas/",
"directory2 = /media/elvee/FILES/LINUX/Klaas/",
"directory3 = /media/FILES/Klaas/",
"directory4 = /media/FILES/LINUX/Klaas/" 
]

def Text():
    print(doublehash)    
    print('''
 ______     _      __        __    ______     ______ 
|  ____|   | |     \ \      / /   |  ____|   |  ____|
| |____    | |      \ \    / /    | |____    | |____ 
|  ____|   | |       \ \  / /     |  ____|   |  ____|
| |____    | |___     \ \/ /      | |____    | |____
|______|   |_____|     \__/       |______|   |______|


This program will delete all .txt files in the USB or 
External drive in a dir called /Klaas. Use this 
program before shutting down Linux
''')
    print(doublehash)

def Find_Dir():
	global directory
	print("Looking for the directory..")
	print("")
	try:
		os.chdir(directory)
		print("Found the directory", directory, "and bound to it.")
		print(singlehash)
	except OSError:
		while True:
			print("Couldn't find the" + directory + ". Are you sure it is mounted?")
			mounted = raw_input("(Y)es or (N)o: ")
			print(singlehash)
			if mounted == "Y":
				break
			elif mounted == "N":
				print("You can try the following directories: ")
				print("")
				for i in list_of_all_dir:
					print(i)
				print(singlehash)
				what_dir = raw_input("What dir do you want to mount to: ")
				os.chdir(what_dir)
				directory = what_dir
				break

			else:
				print("Wrong input. Try again..")
				print(singlehash)
		print(singlehash)
    
def Find_And_Check():
	global directory
	print("Searching for files..")
	for filelist in glob.glob(directory+"*.txt"):
		print(filelist)
	print(singlehash)
	
	while True:
		check = raw_input('''Want to permanently delete
all .txt in this folder?
(Y)es or (N)o: ''')
		if check == "Y":
			for filelist in glob.glob(directory+"*.txt"):
				os.remove(filelist)
				print("Deleted!", filelist)
			print(doublehash)
			exit()
		elif check == "N":
			print("Not deleted.")
			print("Shutting down program..")
			exit()
		else:
			print("Wrong input. Try again..")
			print(singlehash)

Text()
Find_Dir()
Find_And_Check()
import glob
import os

# hashes to be used in most print statements to sort te code in the terminal.
singlehash = '''
######################################################################
'''
doublehash = '''
######################################################################
######################################################################
'''

def Text():
    print(doublehash)    
    print('''
 ______     _      __        __    ______     ______ 
|  ____|   | |     \ \      / /   |  ____|   |  ____|
| |____    | |      \ \    / /    | |____    | |____ 
|  ____|   | |       \ \  / /     |  ____|   |  ____|
| |____    | |___     \ \/ /      | |____    | |____
|______|   |_____|     \__/       |______|   |______|


This program will delete all .txt files on in all the
the folders up to the 10th subfolder. Use with care! 
For safety this code will only print the outputs.
Please uncomment the "os.remove(filelist), to activate."
''')
    print(doublehash)


folder_list = [
"/*/",
"/*/*/",
"/*/*/*/",
"/*/*/*/*/",
"/*/*/*/*/*/",
"/*/*/*/*/*/*/",
"/*/*/*/*/*/*/*/",
"/*/*/*/*/*/*/*/*/",
"/*/*/*/*/*/*/*/*/*/",
"/*/*/*/*/*/*/*/*/*/*/"
]

def Question():
	while True:
		check = raw_input('''Want to permanently delete
all files in all the folders??
(Y)es or (N)o: ''')
		if check == "Y":
			Find_And_Check()
			print(doublehash)
			exit()
		elif check == "N":
			print("Not deleted.")
			print("Shutting down program..")
			exit()
		else:
			print("Wrong input. Try again..")
			print(singlehash)

def Find_And_Check():
	print("Searching for files..")
	for directories in folder_list:
		print "Scanning the following directories: ", directories
		for filelist in glob.glob(directories+"*.*"):
			print "Found: ", filelist
			with open("GlobCommand_Output_file.txt", "a") as textfile:
				textfile.write(filelist+"\n")
			#uncomment this part to not only print but delete.
			#os.remove(filelist)
			#print("removed ", filelist)
		print(singlehash)

Text()
Question()

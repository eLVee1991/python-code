import os
import subprocess

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


This program will delete all the files on in all the
the folders. Use with care! For safety this code will 
only print the outputs. Please uncomment the 
"os.remove(filelist), to activate."
''')
    print(doublehash)

def Question():
	while True:
		check = raw_input('''Want to permanently delete
all files in all the folders??
(Y)es or (N)o: ''')
		if check == "Y":
			Find_And_Check()
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
	#Optional command instead of find: 
	#You can find the content of all files.
	#grep -Ril "text-to-find-here" /
	proc=subprocess.Popen('find / -type f -name "*.*"', shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	with open("FindCommand_Output_file.txt", "a") as textfile:
		textfile.write("Found the following files on the system..: "+"\n\n")
		textfile.write(output+"\n")
		#uncomment this part to not only print but delete.
		#os.remove(filelist)
		#print("removed ", filelist)
	print(singlehash)

Text()
Question()
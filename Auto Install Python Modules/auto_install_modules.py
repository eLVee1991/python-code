#!/usr/bin/env python

# To use this script you need to open up a terminal. cd to the folder
# where the file is located. 
# enter the following: python3 auto_install_modules.py

import subprocess
import time

# hashes to be used in most print statements to sort te code in the terminal.
singlehash = '''
###############################################################################
'''
doublehash = '''
###############################################################################
###############################################################################
'''

# global var where info on raw_input from question_1 is stored for installation
pip_install_p2 = "sudo pip install "
pip_install_p3 = "sudo pip3 install "
pip_install_settings = ''

# global var where info on raw_input from question_1 is stored for upgrading
pip_upgrade_p2 = "sudo pip install -U "
pip_upgrade_p3 = "sudo pip3 install -U "
pip_upgrade_settings = ''

# list of modules to install
modules = [
    "send2trash",
    "requests",
    "beautifulsoup4",
    "selenium",
    "openpyxl",
    "pypdf2",
    "python-docx",
    "imapclient",
    "pyzmail",
    "twilio",
    "pillow",
	"python3-xlib",
    "pyautogui",
    "django",
    "pygame",
    "setuptools"
    ]

def install_modules():
    for i in range(len(modules)):
        subprocess.call(pip_install_settings + str(modules[i]), shell=True)
        print(singlehash)
        print("One module installed.. Installing next module.")
        print(singlehash)    
    print(doublehash)
    print("All modules are installed.")
    print(doublehash)

def update_modules():
    for i in range(len(modules)):
        subprocess.call(pip_upgrade_settings + str(modules[i]), shell=True)
        print(singlehash)
        print("One module updated.. Updating next module.")
        print(singlehash)
    print(doublehash)
    print("All modules are updated")
    print(doublehash)

def text():
    print(doublehash)    
    print('''
 ______     _      __        __    ______     ______ 
|  ____|   | |     \ \      / /   |  ____|   |  ____|
| |____    | |      \ \    / /    | |____    | |____ 
|  ____|   | |       \ \  / /     |  ____|   |  ____|
| |____    | |___     \ \/ /      | |____    | |____
|______|   |_____|     \__/       |______|   |______|


Welkom bij de automatische installer en updater van 
verschillende modules voor Python 2.x en 3.x
''')
    print("Modules:")
    print(modules)
    print('''
note:
"git+https://github.com/metachris/py2app.git@master" 
can only update, not install..''')
    print(doublehash)

def question_1():
    while True:
        question_1 = raw_input('''
        Is pip up-to-date?
        And what about xCode developer commandline tools?

        1 = update pip
        2 = install xCode developer commandline tools
        3 = update all
        4 = no update needed

        type here: ''')
        print(singlehash)

        if question_1 == '1':
            subprocess.call("pip install -U pip; sudo apt-get install python3-pip", shell=True)
            print(singlehash)
        elif question_1 == '2':
            subprocess.call("xcode-select --install", shell=True)
            print(singlehash)
        elif question_1 == '3':
            subprocess.call("pip3 install -U pip", shell=True)
            print(singlehash)
            subprocess.call("xcode-select --install", shell=True)
            print(singlehash)
        elif question_1 == '4':
            break
        else:
            print(singlehash)
            print("wrong input. Try again.")
            print(singlehash)
        

def question_2():
    # Global needs to be raised to change the pip install_upgrade settings var
    global pip_install_settings
    global pip_upgrade_settings
    global modules

    while True:
        question_2 = raw_input('''
        Should I use python 2.x or 3.x?
        Or append an module to the list?

        1 = python 2.x
        2 = python 3.x
		3 = quit.

        type here: ''')
        print(singlehash)

        if question_2 == "1":
            pip_install_settings = pip_install_p2
            pip_upgrade_settings = pip_upgrade_p2
            break
        elif question_2 == "2":
			pip_install_settings = pip_install_p3
			pip_upgrade_settings = pip_upgrade_p3
			break
        elif question_2 == "3":
			exit()
        else:
            print(singlehash)
            print("wrong input. Try again.")
            print(singlehash)

def append():
    module_append = raw_input('''
    What is the name of the module?

    type here: ''')
    print(singlehash)
    modules.append(module_append)
    print(singlehash)

def question_3():
    while True:
        question_3 = raw_input('''
        Should I install or update? 

        1 = install
        2 = update
        3 = add item to list
        4 = quit


        type here: ''')
        print(singlehash)

        if question_3 == "1":
            install_modules()
            exit()
        elif question_3 == "2":
            update_modules()
            exit()
        elif question_3 == "3":
            append()
            print(modules)
            print(singlehash)
            question_2()
        elif question_3 == "4":
            exit()
        else:
            print(singlehash)
            print("wrong input. Try again.")
            print(singlehash)

text()
question_1()
question_2()
question_3()



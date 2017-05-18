#! python3

# Hier een klein scriptje wat je vraagt of een auto macscan wilt uitvoeren.
# De programma's openen pas als de andere gesloten zijn. Laat de muis dus ook op het kruisje drukken of via het toetsenbord (CMD+Q) de boel stoppen.

### Misschien kan ik de code ook omdraaien? autogui aanzetten om alles te laten draaien in eerste instantie. En pas een thread met een timer na de yesno box in de __login_btn functie.
### Als vraag : "Wil je nu scannen of om ...") yes == nu. No == die bepaalde tijd.

# alle modules
from datetime import datetime
import logging
import time
from threading import Timer
import pyautogui

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

# Standaart functies om het scherm mee te bedienen + failsafe.
pyautogui.size()
pyautogui.FAILSAFE = True

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

# losse variabelen die gaan over tijd en tijdberekeing die verderop worden gebruikt.
today = datetime.today()
time_to_run = today.replace(day = today.day, hour = 10, minute = 20, second = 0, microsecond = 0)
delta_time = time_to_run - today
seconds = delta_time.seconds + 1

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

# een reeks hashtags om later op te roepen, om de code te onderscheiden.
singlehash = '''
###############################################################################
'''
doublehash = '''
###############################################################################
###############################################################################
###############################################################################
'''

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

def text():
    print(doublehash)    
    print('''
 ______     _      __        __    ______     ______ 
|  ____|   | |     \ \      / /   |  ____|   |  ____|
| |____    | |      \ \    / /    | |____    | |____ 
|  ____|   | |       \ \  / /     |  ____|   |  ____|
| |____    | |___     \ \/ /      | |____    | |____
|______|   |_____|     \__/       |______|   |______|


Welkom bij de automatisch mac scan. 
Het scant automatischde volgende programma's:

KnockKnock
MalwareBytes
Avast

Druk op 'ctrl+c' om het script te stoppen.''')
    print(doublehash)

#########################################################################################################################################################################

def ScanAtTime():
    pyautogui.alert("WHAT ARE YOU WAITING FOR?", '''Ik zal iedere dag een 
scan voor je uitvoeren om:

10:20''')

    # Maak een logfile aan
    LOG_FILENAME = 'Mac Auto Check.log'
    
    # Wat staat er in de LOGFILE en         
    logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info(today)
    logging.warning("A scan will be run now on KnockKnock, Malware Bytes and Avast.")
    
    # Start een thread met een timer, die het programma opent zodra de timer verstreken is. De timer is gebasseerd op de delta_time en seconds variabele.
    thread_1 = Timer(seconds, ScanThemAll) #, vul hier de naam van def in )
    thread_1.start()

#########################################################################################################################################################################

def StopTheScript():
	# Maak een logfile aan
    LOG_FILENAME = 'Mac Auto Check.log'
    logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info(today)
    
    logging.warning("The script has been stopped by the user.")
    exit()

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

def ScanThemAll():
    pyautogui.click()
    time.sleep(2)
    pyautogui.hotkey("command", "space")   
    time.sleep(1)
    pyautogui.typewrite("Avast")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    print(singlehash)
    print("Please wait for Avast to run")
    print("Starting at: " + str(today))
    print(singlehash)
    a1()
    a2()
    print("Starting KnockKnock while Avast is running in the background")
    KnockKnock()
    print("Starting MalwareBytes while Avast is running in the background")
    MalwareBytes()
    print("Continuing with Avast in Full-Screen.")
    pyautogui.hotkey("fn", "ctrl", "f2")
    time.sleep(1)
    pyautogui.press(["tab", "tab", "tab", "tab"])
    time.sleep(1)
    pyautogui.press(["down, down, down, down"])
    time.sleep(1)
    a3()
    print("Done! at: " + str(today))

    # Maakt een notitie in de logfile
    # Maak een logfile aan
    LOG_FILENAME = 'Mac Auto Check.log'
    logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info(today)
    logging.warning("Scan on Avast, KnockKnock and MalwareBytes are finished.")

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

# Alle functies die met de funcite KnockKnock() samenwerken, zoals de verschillende afbeeldingen die pyautogui zoekt en op klikt.
def KnockKnock():
    time.sleep(1)
    pyautogui.hotkey("command", "space")
    time.sleep(1)
    pyautogui.typewrite("KnockKnock")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    print(singlehash)
    print("Please wait for KnockKnock to run")
    print("Starting at: " + str(today))
    print(singlehash)
    kk1()
    kk2()
    kk3()
    kk4()
    kk5()
    print("Done! at: " + str(today))

    # Maakt een notitie in de logfile
    # Maak een logfile aan
    LOG_FILENAME = 'Mac Auto Check.log'
    logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info(today)
    logging.warning("Scan on KnockKnock is finished.")

#########################################################################################################################################################################

def kk1():
    while True:
        kk1 = pyautogui.locateOnScreen('./Pictures/kk1.png')
        if kk1 == None:
            time.sleep(5)
            print("...")
        else:
            kk1 = pyautogui.center(kk1)
            pyautogui.click(kk1)
            print("Found the 'scan' button.")
            time.sleep(1)
            break
                   
def kk2():
    while True:
        kk2 = pyautogui.locateOnScreen('./Pictures/kk2.png')
        if kk2 == None:
            time.sleep(5)
            print("...")
        else:
            kk2 = pyautogui.center(kk2)
            pyautogui.click(kk2)
            print("Found the 'ok' button.")
            time.sleep(1)
            break
        
def kk3():
    time.sleep(2)
    pyautogui.press("enter")
    print("Saving the file.")
    time.sleep(1)

def kk4():
    while True:
        kk4 = pyautogui.locateOnScreen('./Pictures/kk4.png')
        if kk4 == None:
            time.sleep(5)
            print("...")
        else:
            kk4 = pyautogui.center(kk4)
            pyautogui.click(kk4)
            print("Found the 'replace' button.")
            time.sleep(1)
            break

def kk5():
    time.sleep(1)
    pyautogui.press("enter")
    print("Found the 'ok' button.")
    time.sleep(1)
    pyautogui.hotkey('command', 'q')
    print("Closed the program.")
    time.sleep(1)

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

# Alle functies die met de funcite MalwareBytes() samenwerken, zoals de verschillende afbeeldingen die pyautogui zoekt en op klikt.
def MalwareBytes():
    time.sleep(1)
    pyautogui.hotkey("command", "space")
    time.sleep(1)
    pyautogui.typewrite("MalwareBytes")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    print(singlehash)
    print("Please wait for MalwareBytes to run")
    print("Starting at: " + str(today))
    print(singlehash)
    mb1()
    mb2()
    mb3()
    mb4()
    mb4_1()
    mb5()
    mb6()
    mb7()
    print("Done! at: " + str(today))

    # Maakt een notitie in de logfile
    # Maak een logfile aan
    LOG_FILENAME = 'Mac Auto Check.log'
    logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info(today)
    logging.warning("Scan on MalwareBytes is finished.")

#########################################################################################################################################################################

def mb1():
    while True:
        mb1 = pyautogui.locateOnScreen('./Pictures/mb1.png')
        if mb1 == None:
            time.sleep(5)
            print("...")
        else:
            time.sleep(10)
            mb1 = pyautogui.center(mb1)
            pyautogui.click(mb1)
            print("Found the 'scan' button.")
            time.sleep(1)
            break
        
def mb2():
    while True:
        mb2 = pyautogui.locateOnScreen('./Pictures/mb2.png')
        if mb2 == None:
            time.sleep(5)
            print("...")
        else:
            mb2 = pyautogui.center(mb2)
            pyautogui.click(mb2)
            print("Found the 'close' button.")
            time.sleep(1)
            break

def mb3():
    time.sleep(5)
    pyautogui.hotkey("fn", "ctrl", "f2")
    time.sleep(1)
    pyautogui.press(["tab", "tab", "tab", "tab"])
    time.sleep(1)
            
def mb4():
    pyautogui.press(["down", "down", "down"])
    pyautogui.press("enter")
    print("Found the 'system scan' button.")
    time.sleep(1)

def mb4_1():
    while True:
        mb4 = pyautogui.locateOnScreen('./Pictures/mb4.png')
        if mb4 == None:
            time.sleep(5)
            print("...")
        else:
            pyautogui.hotkey("command", "p")
            print("Printing results.")
            time.sleep(1)
            break

def mb5():
    while True:
        mb5 = pyautogui.locateOnScreen('./Pictures/mb5.png')
        if mb5 == None:
            time.sleep(5)
            print("...")
        else:
            mb5 = pyautogui.center(mb5)
            pyautogui.click(mb5)
            print("Creating and saving pdf.")
            time.sleep(1)
            pyautogui.press("down")
            pyautogui.press("down")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.typewrite("MalwareBytes_SystemSnapshot")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            break

def mb6():
    while True:
        mb6 = pyautogui.locateOnScreen('./Pictures/mb6.png')
        if mb6 == None:
            time.sleep(5)
            print("...")
        else:
            mb6 = pyautogui.center(mb6)
            pyautogui.click(mb6)
            print("Replacing the file.")
            time.sleep(1)
            break

def mb7():
    while True:
        mb7 = pyautogui.locateOnScreen('./Pictures/mb7.png')
        if mb7 == None:
            time.sleep(5)
            print("...")
        else:
            time.sleep(1)
            pyautogui.hotkey("command", "q")
            print("Closing the program.")
            time.sleep(1)
            break

#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

# Alle functies die met de funcite Avast() samenwerken, zoals de verschillende afbeeldingen die pyautogui zoekt en op klikt.
def Avast():
    time.sleep(2)
    pyautogui.hotkey("command", "space")   
    time.sleep(1)
    pyautogui.typewrite("Avast")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    print(singlehash)
    print("Please wait for Avast to run")
    print("Starting at: " + str(today))
    print(singlehash)
    a1()
    a2()
    a3()
    print("Done! at: " + str(today))

    # Maakt een notitie in de logfile
    # Maak een logfile aan
    LOG_FILENAME = 'Mac Auto Check.log'
    logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info(today)
    logging.warning("Scan on Avast is finished.")

#########################################################################################################################################################################

def a1():
    while True:
        a1 = pyautogui.locateOnScreen('./Pictures/a1.png')
        if a1 == None:
            time.sleep(5)
            print(" ")
            print("...")
        else:
            a1 = pyautogui.center(a1)
            pyautogui.click(a1)
            print("Found the 'scan' button.")
            time.sleep(1)
            break
        
def a2():
    while True:
        a2 = pyautogui.locateOnScreen('./Pictures/a2.png')
        if a2 == None:
            time.sleep(5)
            print("...")
        else:
            a2 = pyautogui.center(a2)
            pyautogui.click(a2)
            print("Found the 'button'.")
            time.sleep(1)
            break
        
def a3():
    while True:
        a4 = pyautogui.locateOnScreen('./Pictures/a4.png')
        if a4 == None:
            time.sleep(5)
            print("...")
        else:
            a4 = pyautogui.center(a4)
            pyautogui.click(a4)
            print("Closing the program.")
            time.sleep(1)
            pyautogui.hotkey("command", "q")
            break


#########################################################################################################################################################################
#########################################################################################################################################################################
#########################################################################################################################################################################

while True:
    text()
    question = input('''
Welke scan moet ik uitvoeren?

1. KnockKnock
2. Malware Bytes
3. Avast
4. Scan Them All!
5. Scan Them All at 10.20
6. Please make it stop!

Antwoord hier: ''')
    
    if question == "1":
        KnockKnock()
    elif question == "2":
        MalwareBytes()
    elif question == "3":
        Avast()
    elif question == "4":
        ScanThemAll()
    elif question == "5":
        ScanAtTime()
    elif question == "6":
    	StopTheScript()
    else:
        time.sleep(5)
        print('''
Verkeerd antwoord. Antwoord met 1, 2, 3, 4 of 5.
''')


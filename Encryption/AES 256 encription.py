"""
This script will encrypt all files in a folder with AES256
Put this file in the same dir as the file you want to encrypt/decrypt.
"""


# import the modules. This will use AES (Advanced Encryption Standard)
# We will use AES256 for the best encryption
# We will hash the password key for better protection via SHA256
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys, pkg_resources

# This function will encrypt the file. It will take a key and a filename 
def encrypt(key, filename):
        #This is the chunksize we will pull from the file.
        # Adding 64*1024 saves us from typing the amount of bytes by ourselves
        chunksize = 64 * 1024
        #Gets the outfile
        outFile = "(encrypted)"+filename

        """
        #Only use this method if you want to encrypt all the files. Delete the var above.
        #The outputfile saves the file in the same directory and adds "encrypted" in front on the file
        outFile = os.path.join(os.path.dirname(filename), "(encrypted)"+os.path.basename(filename))
        """

        #Gets the size of the file and
        filesize = str(os.path.getsize(filename)).zfill(16)

        # Creates a var IV which is for now set to None
        IV = ''
 
        #We want a 16bytes IV.
        for i in range(16):
                IV += chr(random.randint(0, 0xFF))
       
        # This var wil will take a key as input, and uses AES CBC 
        #(Chained Block Cipher) as the standard and the randomized IV created before.
        encryptor = AES.new(key, AES.MODE_CBC, IV)
 
        #Open the file as binary as var "infile"
        with open(filename, "rb") as infile:
                #Open the outputfile as var "outfile" to dump our data in.
                with open(outFile, "wb") as outfile:
                        #Output the filesize
                        outfile.write(filesize)
                        #Add the IV so we can read the file later.
                        outfile.write(IV)

                        #Keep encrypting the data in the file till it's all done.
                        while True:
                                #This var reads the chunksize of the infile
                                chunk = infile.read(chunksize)
                                #If the lenght of the chunksize of our infile is 0. Break the loop.
                                if len(chunk) == 0:
                                        break
                                #If it's not 0 add some padding (spaces in this case)
                                elif len(chunk) % 16 !=0:
                                        #If the chunks are less then 16 add the spaces.
                                        chunk += ' ' *  (16 - (len(chunk) % 16))
 
                                #Write the output of the encryptor (of the chunk). This will write the encrypted chunk.
                                outfile.write(encryptor.encrypt(chunk))
 

# The function decrypt will also take a key and a filename. 
def decrypt(key, filename):
        #This is the chunksize we will pull from the file.
        # Adding 64*1024 saves us from typing the amount of bytes by ourselves
        chunksize = 64 * 1024
        #The outputfile saves the file in the same directory and deletes "encrypted" from the file
        outFile = filename[11:]

        """
        #Only use this method if you want to use this program to encrypt all the files. Delete the other var.
        #The outputfile saves the file in the same directory and deletes "encrypted" from the file
        outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))
        """
        #Open the file as binary as var "infile"
        with open(filename, "rb") as infile:
                #Reads the file in chunks of 16 bytes at the time
                filesize = infile.read(16)
                #The IV needs to equal the infile
                IV = infile.read(16)
 
                #Creates a decryptor var
                decryptor = AES.new(key, AES.MODE_CBC, IV)
                #Opens the output file as read binary.
                with open(outFile, "wb") as outfile:
                        #Keeps decrypting the data in the file till it's all done.
                        while True:
                                #This var reads the chunksize of the infile
                                chunk = infile.read(chunksize)
                                #Breaks the loop if the chunks of the file are equal to 0.
                                if len(chunk) == 0:
                                        break
                                #Write the outputfile to the same dir.
                                outfile.write(decryptor.decrypt(chunk))
                        #It will save the file as the same size as the original size.
                        outfile.truncate(int(filesize))

#If you want the encrypt all the files. Use this below.
"""       
def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd()):
                for names in files:
                        allFiles.append(os.path.join(root, names))
 
        return allFiles
 
       
choice = raw_input("Do you want to (E)ncrypt or (D)ecrypt? ")
password = raw_input("Enter the password: ")
 
encFiles = allfiles()

if choice == "E":
        for Tfiles in encFiles:
                if os.path.basename(Tfiles).startswith("(encrypted)"):
                        print "%s is already encrypted" %str(Tfiles)
                        pass
 
                elif Tfiles == os.path.join(os.getcwd(), sys.argv[0]):
                        pass
                else:
                        encrypt(SHA256.new(password).digest(), str(Tfiles))
                        print "Done encrypting %s" %str(Tfiles)
                        os.remove(Tfiles)
 
 
elif choice == "D":
        filename = raw_input("Enter the filename to decrypt: ")
        if not os.path.exists(filename):
                print "The file does not exist"
                sys.exit(0)
        elif not filename.startswith("(encrypted)"):
                print "%s is already not encrypted" %filename
                sys.exit()
        else:
                decrypt(SHA256.new(password).digest(), filename)
                print "Done decrypting %s" %filename
                os.remove(filename)
 
else:
        print "Please choose a valid command."
        sys.exit()
        """

def getKey(password):
        hasher = SHA256.new(password)
        return hashes.digest()

def main():
        while True:
                choice = input('''
Would you like to (E)ncrypt or (D)ecrypt? Or (S)top the program?
Enter E, D, S: ''')
        
                if choice == "E":
                        filename = input("Enter a file to encrypt :")
                        password = input("Enter the password: ")
                        print("Encrypting the file now. Please wait.. ")
                        encrypt(getKey(password), filename)
                        print("Done encrypting the file..")
                elif choice == "D":
                        filename = input("Enter a file to decrypt: ")
                        password = input("Enter the password: ")
                        print("Decrypting the file now. Please wait.. ")
                        decrypt(getKey(password), filename)
                        print("Done decrypting the file..")
                elif choice == "S":
                        print("Stopping the program now..")
                        exit()
                else:
                        print("No option selected. Please try again.")

if __name__ == "__main__":
        main()
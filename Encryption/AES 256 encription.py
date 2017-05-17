from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, sys

def encrypt(key, filename):
	chunksize = 64 * 1024
	outFile = os.path.join(os.path.dirname(filename), "(ecrypted)"+os.path.basename(filename))
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = ""

	for i in range(16):
		IV += chr(random.int(0, 0xFF))

	encryption = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, "rb") as infile:
		with open(outFile, "wb") as outfile:
			outfile.write(filesize)
			outfile.write(IV)
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += " " * (16 - (len(chunk) % 16))

				outfile.write(encryption.encrypt(chunk))

def decrypt(key, filename):
	outFile = os.path.join(os.path.dirname(filename), os.path.basename(filename[11:]))
	chunksize = 64 * 1024
	with open(filename, "rb") as infile:
		filesize = infile.read
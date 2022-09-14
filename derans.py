import os
from cryptography.fernet import Fernet

## finding files first

files = [] # empty list

for file in os.listdir():
	if file == "rans.py" or file == ".encryption_key.key" or file == "derans.py":	
	# so that we dont encrpt ourselves
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

#key = Fernet.generate_key()
#print(key)

with open(".encryption_key.key",'rb') as mykey:
	secret = mykey.read()

print(secret)
# reading the key

for file in files:
	with open(file,'rb') as thefile:
		contents = thefile.read()
	contents_decrypted = Fernet(secret).decrypt(contents)
	with open(file,'wb') as thefile:
		thefile.write(contents_decrypted)
 



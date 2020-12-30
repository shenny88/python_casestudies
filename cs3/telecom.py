import os.path
from os import path
from cryptography.fernet import Fernet

# Generating the key and writing it to a file
def genwrite_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def call_key():
    return open("secret.key", "rb").read()

def encrypt_data(slogan):
    genwrite_key()
    key = call_key()
    a = Fernet(key)
    coded_slogan = a.encrypt(slogan)
    return coded_slogan

def decrypt_data(coded_slogan):
    key = call_key()
    b = Fernet(key)
    decoded_slogan = b.decrypt(coded_slogan)
    return decoded_slogan


print("\t\t****SIM Verification Portal: User****\t\t")
print("FingerPrint: ")
name = input("Enter Your Name(Fingerprint): ")

length = 0
while length != 12:
    refid = input("Enter Reference Id: ")
    length = len(refid)
    if length != 12:
        print("Reference ID should be 12 digits")
    if not refid.isalnum():
        print("Reference ID should contain onlyb alphanumeric values")
        length = 0

if not os.path.isfile("secret.key"):
    genwrite_key()
enc = encrypt_data(refid.encode())
dec = decrypt_data(enc)

user_data = { name : enc }
print("Encrypted customer data against fingerprint: %s" %(user_data))








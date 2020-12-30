from cryptography.fernet import Fernet

print("\t\t****SIM Verification Portal****\t\t")
print("FingerPrint: ")
name = input("Enter Your Name: ")

length = 12
while length != 12:
    refid = input("Enter Reference Id: ")
    length = len(refid)
    if length != 12:
        print("Reference ID should be 12 digits")
    if not refid.isalnum():
        length = 0



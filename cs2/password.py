username=input("Enter username: ")
password=input("Enter password: ")
l = 0
d = 0
u = 0
s = 0

# checking minimum and maximum length of password
if not len(password) >= 6:
    print("Minimum password length is 6")
if not len(password) <= 12:
    print("Maximum password length is 12")

# checking atleast 1 letter [a-z]

for letter in password:
    if letter.islower():
        l = l + 1
    if letter.isdigit():
        d = d + 1
    if letter.isupper():
        u = u + 1
    if letter in {"$", "#", "@"}:
        s = s + 1

if l < 1:
    print("Password must contain atleast 1 letter between [a-z]")

if d < 1:
    print("Password must contain atleast 1 number between [0-9]")

if u < 1:
    print("Password must contain atleast 1 letter between [A-Z]")

if s < 1:
    print("Password must contain atleast 1 charcted from [$#@]")


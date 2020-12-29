import sys

# defining list variables
factors = []
even = []
odd = []

# checking minimum number os arguments is passed or not
if len(sys.argv) < 2:
    print("need minimum 1 argument")
    exit(100)
else:
    number = sys.argv[1]

# print factors
counter = 1
while int(number) != counter:
    if int(number) % counter == 0:
        factors.append(counter)
        if counter % 2:
            odd.append(counter)
        else:
            even.append(counter)
    counter = counter + 1

print("factors of ",number," are:" , factors)
print("Even factors are ", even)
print("Odd factors are ", odd)
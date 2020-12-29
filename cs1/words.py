userinput = input("Input: ")
words = userinput.split()
words.sort()
print("Output: ")
for i in words:
    print(i, end=" ")

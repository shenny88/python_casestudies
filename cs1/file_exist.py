import os.path

# myfile = open("sample.txt","w")
# myfile.write("this is a demo")
# myfile.close()

if os.path.isfile("sample.txt"):
    print("file exist")
else:
    print("file does not exist")


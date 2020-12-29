str = input("Enter string: ")
str2 = str
count = len(str)
i = 0

while count > 0:
    if i <= len(str2):
        if str2:
            j = str2[i]
    char_count = str2.count(j, 0, len(str2))
    print("%s,%s" % (j, char_count))
    count = count - char_count
    str2 = str2.replace(j, "")

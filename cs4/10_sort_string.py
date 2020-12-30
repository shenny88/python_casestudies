# 10. Write a program that accepts a comma separated sequence of words as input and
#    prints the words in a comma-separated sequence after sorting them alphabetically.
mystr = input("Enter string seperated by comma: ")
mystr_list = sorted(mystr.split(","))
print(",".join(mystr_list))




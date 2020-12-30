# 7. program which can compute the factorial of a given numbers. Use recursion
# to find it.
import sys

def factorial(mynum):
    if mynum == 1:
        return 1
    else:
        mynum = mynum * factorial(mynum -1)
    return(mynum)

num = int(sys.argv[1])
print(factorial(num))


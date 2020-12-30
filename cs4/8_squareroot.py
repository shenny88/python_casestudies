#8.  Program that calculates and prints the value according to the given formula:
#    Q = Square root of [(2 * C * D)/H]
#    Following are the fixed values of C and H: C is 50. H is 30.
#    D is the variable whose values should be input to your program in a comma-
#    separated sequence
import math

C = 50
H = 30
D = "100,150,180"
D_list = D.split(",")

for item in D_list:
    Q = math.sqrt((2 * C * int(item)) / H)
    Q = print(math.floor(Q),end=" , ")

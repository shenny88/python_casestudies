# 6. Write a program which will find all such numbers which are divisible by 7 but are
#   not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained
#   should be printed in a comma-separated sequence on a single line.

lower_limit = 2000
upper_limit = 3200 + 1

for number in range(lower_limit, upper_limit):
    if number % 7 == 0:
        if number % 5 != 0:
            print(number, end=",")


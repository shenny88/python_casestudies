import sys

num = int(sys.argv[1])
reverse = 0
input_number = num
while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10

if input_number == reverse:
    print("PALINDROME!!!")
else:
    print("NOT A PALINDROME!!!")

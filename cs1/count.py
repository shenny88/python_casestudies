import sys

string = sys.argv[1]
digit_count = 0
letter_count = 0

for i in string:
    if i.isdigit():
        digit_count = digit_count + 1
    else:
        letter_count = letter_count + 1

print("Number of digits: " , digit_count)
print("Number of letters: " , letter_count)
console_input = input("Enter your String: ")
string_length = len(console_input)

for i in range(0,string_length):
    if i % 2 == 0:
        print(console_input[i],end="")


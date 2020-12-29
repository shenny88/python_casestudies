list1=[]
lower_limit=1
upper_limit=1000+1

for i in range(lower_limit,upper_limit):
    if i % 5 == 0 and i % 7 == 0:
        list1.append(i)

print(list1)
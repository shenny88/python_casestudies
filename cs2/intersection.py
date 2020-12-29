list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]
list3 = []

for i in list1:
    if i in list2:
        list3=[i]

print(list3)

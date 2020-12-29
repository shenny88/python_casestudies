list1 = [12, 24, 35, 70, 88, 120, 155]
length = len(list1)
list2 = [list1[i] for i in range(0, length) if i != 0 and i != 4 and i != 5]
print(list2)

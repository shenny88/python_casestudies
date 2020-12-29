list1 = [12, 24, 35, 70, 88, 120, 155]
list2 = [ i for i in list1 if not i%5==0 and not i%7==0]
print(list2)

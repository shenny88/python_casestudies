num=input("enter num:")
myinput=int(num)
out=0
for i in range(1,myinput+1):
    out=out+(i/(i+1))
print(out)
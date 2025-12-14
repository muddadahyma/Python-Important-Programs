num=4321
res=0
while num>0:
    digit=num%10
    res=res*10+digit
    num=num//10
print(res)


num=input("enter value: ")
print(str(num)[::-1])


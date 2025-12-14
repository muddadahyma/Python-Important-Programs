num=int(input("enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not a armstrong number")



num=int(input("enter a number: "))#9474
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+(digit**order)
    temp=temp//10
if sum==num:
    print(num,"is armstrong number")
else:
    print(num,"is not a armstrong number")
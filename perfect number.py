"""
num=int(input("enter number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"is not a perfect number")"""



min=int(input("enter minimum number: "))
max=int(input("enter maximum number: "))
for num in range(min,max):

    if num>1:
        sum = 0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        print(num,"is perfect number")



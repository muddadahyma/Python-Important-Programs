#1----------------------------------------

num=int(input("enter a number: "))
count=0
for i in range(2,num):
    #print("iteration-" , i)
    if num%i==0:
        count=1
        break
if count==1:
    print("not prime")
else:
    print("prime")

#2--------------------------------------------------

    n = int(input("enter a number: "))
    for num in range(2, n + 1):

        count = 0
        for i in range(2, num):
            if num % i == 0:
                count = 1
                break
        if count == 1:
            print(num, "is not a prime")
        else:
            print(num, "is  a prime")



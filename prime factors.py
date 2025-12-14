num=int(input("enter number: "))
for i in range(1,num+1):
    if num%i==0:
        count=0
        for k in range(1,i+1):
            if i%k==0:
                count=count+1

        if count==2:
            print(i)

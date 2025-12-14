#1====armstrong
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

#2=====palindrome
num=int(input("enter a number: "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=(sum*10)+digit
    temp=temp//10
if sum==num:
    print(num,"is palindrome")
else:
    print(num,"is  not palindrome")

#3=====even odd
for i in range(1,100):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

#4====perfect number
num=int(input("enter number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"is not a perfect number")

#5====prime upto given number
n=int(input("enter a number: "))
for num in range(2,n+1):
    count=0
    for i in range(1,num+1):
         if num%i==0:
            count+=1
    if count==2:
        print(num)

#6====prime upto min to max number
start=int(input("enter starting number: "))
end=int(input("enter ending number: "))
for num in range(start,end+1):
    is_prime=True
    for i in range(2,num):
         if num%i==0:
            is_prime = False
            break
    if is_prime:
        print(num)


#7====fibonacci
n=int(input("enter number: "))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b

#8===factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num=int(input("enter a number: "))
print(factorial(num))

#9======positive or negative
num=int(input("enter a number: "))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative number")
else:
    print("Zero")

#10=====reverse a number
#1======
num=4321
res=0
while num>0:
    digit=num%10
    res=res*10+digit
    num=num//10
print(res)
#2reverse
num=input("enter value: ")
print(str(num)[::-1])

#11====swapping
a=int(input("enter number: "))
b=int(input("enter number: "))
temp=a
a=b
b=temp
print("after swapping")
print(a)
print(b)

#12====array addition
A=[[6,2,1],[4,1,2],[9,2,1]]
B=[[1,2,3],[4,6,7],[3,7,4]]
C=[[0,0,0],[0,0,0],[0,0,0]]
print("print A matrix")
print(A)
print("print B matrix")
print(B)
for i in range(3):
    for j in range(3):
        C[i][j]=A[i][j]+B[i][j]
print("addition of A,B matrix")
for row in C:
    print(row)

#13===element found in array
arr = [10, 20, 30, 40, 50]
x = 59
found = False
for i in range(len(arr)):
    if arr[i] == x:
        print("Element found in the array")
        found = True
        break
if not found:
    print( "not found in the array.")


#14===prime factors
num=int(input("enter number: "))
for i in range(1,num+1):
    if num%i==0:
        count=0
        for k in range(1,i+1):
            if i%k==0:
                count=count+1

        if count==2:
            print(i)






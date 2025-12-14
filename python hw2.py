"""1====perfect number

num=int(input("enter number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"is not a perfect number")

output:
enter number: 6
6 is perfect number


2====perfect numbers min to max
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

output:
enter minimum number: 4
enter maximum number: 1000
6 is perfect number
28 is perfect number
496 is perfect number


3====prime number min to max
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

output:
enter starting number: 2
enter ending number: 50
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47


birthday = "10-04-2004"
print("Happy Birthday Hyma!🎉")
print("Your birthday is on:", birthday)
sql=int(input("Enter the sql marks:"))
java=int(input("Enter the java marks"))
python=int(input("Enter the python marks:"))
print("Your B.Tech grade marks are:")
print("SQL: ", sql)
print("Java: ", java)
print("Python: ", python)
if sql > java and sql > python:
    print("You scored highest in SQL.")
elif java > sql and java > python:
    print("You scored highest in Java.")
elif python > sql and python > java:
    print("You scored highest in Python.")
else:
    print("There is a tie in your highest marks.")

output:
Happy Birthday Hyma!🎉
Your birthday is on: 10-04-2004
Enter the sql marks:70
Enter the java marks80
Enter the python marks:81
Your B.Tech grade marks are:
SQL:  70
Java:  80
Python:  81
You scored highest in Python.
"""

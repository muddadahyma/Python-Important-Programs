
#1--------------
"""num=int(input("enter a number: "))
fib=[0,1]
for i in range(2,num):
    fib.append(fib[-1]+fib[-2])
print(fib[:num])"""

#2----------------------
"""
num=15
fib=[0,1]
for i in range(2,num):
    fib.append(fib[-1]+fib[-2])
print(fib[:num])"""

n=int(input("enter number: "))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b


"""1=====Hello World
print("hello word")


2======sum
a=int(input("enter a value: "))
b=int(input("enter b value: "))
sum=a+b
print(sum)

output:
enter a value: 10
enter b value: 20
30

3======operators
a=int(input("enter a value: "))
b=int(input("enter b value: "))
print("Addition:",a+b)
print("subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Remainder:",a%b)
print("Exponentiation:",a**b)
print("Floor Division:",a//b)

output:
enter a value: 10
enter b value: 20
Addition: 30
subtraction: -10
Multiplication: 200
Division: 0.5
Remainder: 10
Exponentiation: 100000000000000000000
Floor Division: 0

4====swapping
a=int(input("enter number: "))
b=int(input("enter number: "))
print("before swapping")
print(a)
print(a)
temp=a
a=b
b=temp
print("after swapping")
print(a)
print(b)

5=====even or odd
num=int(input("enter a number: "))
if num%2==0:
        print(num,"is even")
else:
        print(num,"is odd")


6====student result
T=int(input("enter telugu marks:"))
E=int(input("enter english marks:"))
H=int(input("enter hindi marks:"))
M=int(input("enter maths marks:"))
S=int(input("enter social marks:"))
sum=T+E+H+M+S
avg=sum/5
if avg>=90:
    print("out standing performance")
elif avg>=80 and avg<=89:
    print("A grade")
elif avg>=70 and avg<=70:
    print("B grade")
elif avg>=60 and avg<=69:
    print("C grade")
elif avg>=50 and avg<=59:
    print("D grade")
elif avg>=40 and avg<=49:
    print("Pass")
else:
    print("Fail")

output:
enter telugu marks:79
enter english marks:80
enter hindi marks:98
enter maths marks:90
enter social marks:70
A grade


7======square roots
import cmath
print("enter the equation values: ")
a=float(input("enter a value: "))
b=float(input("enter b value: "))
c=float(input("enter c value: "))
d=(b*b)-(4*a*c)
if d==0:
    print("roots are real and equal")
    root1=-b/(2*a)
    root2=-b/(2*a)
    print("root1: ",root1)
    print("root2: ",root2)
elif(d>0):
    print("roots are real and different")
    root1 = -b+cmath.sqrt(d)/(2*a)
    root2 = -b-cmath.sqrt(d)/(2*a)
    print("root1: ", root1)
    print("root2: ", root2)
else:
    print("roots are imaginary")

output:
enter the equation values:
enter a value: 2
enter b value: 8
enter c value: 1
roots are real and different
root1:  (-6.12917130661303+0j)
root2:  (-9.87082869338697+0j)
"""




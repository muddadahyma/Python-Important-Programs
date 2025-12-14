"""
1-------
s="lavbhav"
if s==s[::-1]:
    print(s,"is palindrome")
else:
    print(s,"is not  palindrome")


2---------
s=input("enter a string: ")
if s==s[::-1]:
    print(s,"is palindrome")
else:
    print(s,"is not  palindrome")

3-----------

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
"""

num=543
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10
if sum==num:
      print(num,"is palindrome")
else:
    print(num,"is not palindrome")



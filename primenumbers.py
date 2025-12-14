#1 ***********imp------------------------------------me
"""n = int(input("enter a number: "))
for num in range(2, n + 1):

        count = 0
        for i in range(2, num):
            if num % i == 0:
                count = 1
                break
        if count != 1:
            print(num)
            """


#2-----------------------------------

n=int(input("enter a number: "))
for num in range(2,n+1):
    is_prime=True
    for i in range(2,num):
         if num%i==0:
            is_prime = False
            break
    if is_prime:
        print(num)

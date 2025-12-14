def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num=int(input("enter a number: "))
print(factorial(num))
print("testing pull request")


"""without recursion-------------------------




# Example usage
num = 5
print(f"Factorial of {num} is {factorial_iterative(num)}")
"""

arr = [16,24,37,19,41,24,16,32,24,17]
n = int(input("Enter the number to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == n:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found in the list.")
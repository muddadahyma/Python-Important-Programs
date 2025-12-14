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

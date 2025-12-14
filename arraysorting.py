
arr=[76, 23, 45, 12, 54, 9]
print("Original array:", arr)

for i in range(0, len(arr)):
	for j in range(i+1, len(arr)):
		if arr[i] >= arr[j]:
			arr[i], arr[j] = arr[j],arr[i]

print("Sorted List", arr)


"""arr[i], arr[j] = arr[j], arr[i]-------------------same as below-
temp=arr[i]
arr[i]=arr[j] 
arr[j]=temp 
"""
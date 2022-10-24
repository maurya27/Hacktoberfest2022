array = [14, 4 , 56, 2, 100, 97]
l = len(array)

for i in range(l-1):
    for j in range(l-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)

"""def bubblesort(items):
	swapped = False
	# Looping from size of array from last index[-1] to index [0]
	for n in range(len(items)-1, 0, -1):
		for i in range(n):
			if items[i] > items[i + 1]:
				swapped = True
				# swapping data if the element is less than next element in the array
				items[i], items[i + 1] = items[i + 1], items[i]	
		if not swapped:
			# exiting the function if we didn't make a single swap
			# meaning that the array is already sorted.
			return

items = [39, 12, 18, 85, 72, 10, 2, 18]

print("Unsorted list is,")
print(items)
bubblesort(items)
print("Sorted Array is, ")
print(items)
"""
array = [14, 4 , 56, 2, 100, 97]
l = len(array)

for i in range(1, l):
    j = i
    while j>0 and array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
        j -= 1

print(array)

"""
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i]

		
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


#sorting the array [10,34,24,28,31] using insertionSort
arr = [10,34,24,28,31]
insertionSort(arr)
lst = [] 
print("Sorted array is : ")
for i in range(len(arr)):
	lst.append(arr[i])	 
print(lst)


"""
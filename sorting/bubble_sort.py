#works by repeatedly swapping the adjacent elements if they are in wrong order.

#travaerse through array
#if element is > than previous element swipe
#swipe until end of array

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in correct position
        for j in range(0, n - i - 1):
            # if current element is > than next element swipe
            if arr[j] > arr[j + 1]:
                #swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print(arr[i])


#sorting goes through n-1 iterations, looking at n-1 pairs of adjacent elements. O(n2)

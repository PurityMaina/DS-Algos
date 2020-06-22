#place the maximum element at the end. This is repeated until the array is sorted.
#min-heap is a tree-based data structure in which every node is smaller that all of its children
#n is the size of the array
def heapify(arr, n, index):
    largest = index  # Initialize largest as root
    # kusaidia kupanga visualization

    left = 2 * index + 1
    right = 2 * index + 2

    # See if left child of root exists and is
    # greater than root
    if left < n and arr[index] < arr[left]:
        largest = left

        # See if right child of root exists and is
    # greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

        # Change root, if needed
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size
def heapSort(arr): #this is how we fix the broken heap by extracting largest element to root
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Driver code to test above
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
print ("Sorted array is")
for i in range (len(arr)):
    print(arr[i])


#sorting goes through n-1 iterations, looking at n-1 pairs of adjacent elements O(n log n).

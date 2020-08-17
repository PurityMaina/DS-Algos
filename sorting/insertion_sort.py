#travaerse through array
#compare with the next element
#if smaller, shift elements in the sorted sublist
# insert value in the sorted sublist.

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        element_to_sort = arr[i]
        sorted_element = i-1
        while sorted_element >= 0 and element_to_sort < arr[sorted_element]:
            arr[sorted_element + 1] = arr[sorted_element] #add item to sorted array
            sorted_element -= 1 # incrementally sort down the list
        arr[sorted_element + 1] = element_to_sort #if it is greater than, move up and add to sorted element



# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])

#O(n)
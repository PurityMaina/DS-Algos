#traverse through the array
#array is sorted and small

def linearSearch(arr, x):

    for i in len(arr):
        if i == x:
            return i
    return -1

#O(n)
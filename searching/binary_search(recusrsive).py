#recusrsive is kinda like the russian doll or fibonacci sequence
#repetion of a procedure in smaller instances
#divide array into 2 halves
#if < then left if > right
#half again till you find the number

def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        #if element is less than mid then traveserve the left subarray
        elif x < arr[mid]:
            return binary_search(arr, low, mid-1, x)
        #if element is greater than mid then traveserve the right subarray
        elif x > arr[mid]:
            return binary_search(arr, mid + 1, high, x)
        # Element is not present in the array
        else:
            return -1

# Test array
arr = [2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

#recursive implementation, O(Logn) recursion call stack space.
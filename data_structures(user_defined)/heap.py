# a complete binary tree-based data structure
# max heap - value of each node is less than or equal to the value of the parent
# min heap - value of each node is greater than or equal to the value of its parent

import heapq

#initialize list
elements = [7, 6, 8, 0, 9, 12]

# conert list to heap
heapq.heapify(elements)
print("The created heap is:", list(elements))

#push elements into heap
heapq.heappush(elements, 4)
print("The pushed item into heap is:", list(elements))

#Pop elements from heap
heapq.heappop(elements)
print("The popped element from heap is:", heapq.heappop(elements))

#largest element
heapq.nlargest(1,elements)
print ("The 2 largest numbers in the list are: ", heapq.nlargest(2,elements))
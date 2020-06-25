# FIFO data structure
#from collections import deque

# Initializing a queue
#q = deque()
#Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow conditiont
#Dequeue: Removes an item from the queue.
#Front: Get the front item from queue
#Rear: Get the last item from queue

presidents = []

# adding elements to the queue
presidents.append('Jommo')
presidents.append('Moi')
presidents.append('Kibaki')
presidents.append('Uhuru')

print('Presidents are', presidents)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(presidents.pop(0))
print(presidents.pop(0))

print("\nQueue after removing elements")
print(presidents)

# elements can be sorted or unsorted
# elements can contain duplicates and or unique elements
# start at traversing from root and work your way (linear)
# a piece od data and a link to the next node
# each node contains data and a pointer to the next node
class Node:
    #initialize node object
    def __init__(self, data=None):
        self.data = data #initialize data
        self.next = None #set next as none


class SLinkedList:
    #initialize linked list
    def __init__(self):
        self.head = None

    def printlist(self):
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next

items = SLinkedList()
items.head = Node('Monday')
item2 = Node('Tuesday')
item3 = Node('Wednesday')

# link first node to second node
items.head.next = item2

# link second node to third node
item2.next = item3

items.printlist()

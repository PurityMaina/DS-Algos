class Node():
    def __init__(self, data =None):
        self.data = data
        self.next = None

class SLinkedList():
    def __init__(self):
        self.head = None

    def printlist(self):
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next

    def deleteNode(self, position):

        #if linked list is empty
        if self.head == None :
            return

        # Store head node
        curr_node = self.head

        #if head node needs to be deleted
        if curr_node and curr_node.data == position:
            self.head = curr_node.next #setting the head to the next node
            curr_node = None #get rid of the head
            return

        # if node to be deleted is not head
        prev = None # initialize previous node to none
        while curr_node and curr_node.data !=position: #while head node is not none and the item is not the position we are looking for
            prev = curr_node
            curr_node = curr_node.next #move pointer along

        #if the element is not found in the item list
        if curr_node is None:
            return

        #in this case the item is in the list
        prev.next = curr_node.next # previous node points to the next next item
        curr_node = None


items = SLinkedList()
items.head = Node('Monday')
item2 = Node('Tuesday')
item3 = Node('Wednesday')

items.head.next = item2
item2.next = item3

items.deleteNode('Monday')
items.printlist()




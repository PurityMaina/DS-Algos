class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next

    def AtBegining(self, data):
        NewNode = Node(data)

        # Update the new nodes next val to existing node
        NewNode.next = self.head
        self.head = NewNode

items = SLinkedList()
items.head = Node('Monday')
item2 = Node('Tuesday')
item3 = Node('Wednesday')

items.head.next = item2
item2.next = item3

items.AtBegining('Sunday')
items.printlist()



# each node has atleast 2 children
# complete btree - every level is filled other than the last level
# full btree - every node has 2 or 0 children
# trees may be traversed depth-first or breadth-first ie non-linear.
# depth-first traversals - pre(RoLR-1245367), in(LRoR-4251637) and post order(LRRo- 4526731) traversal
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root) #the value passed into a node and setting that as root

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, " ")

        elif traversal_type == ("inorder"):
            return self.inorder_print(tree.root, " ")

        elif traversal_type == ("postorder"):
            return self.postorder_print(tree.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")

    def preorder_print(self, start, traversal):
        if start:#if root is not empty
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal) #recursive call
            traversal = self.preorder_print(start.right, traversal)  # recursive
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


#              1
#            /  \
#           2    3
#          / \   / \
#         4   5  6   7
#

tree = BinaryTree(1)
tree.root.left = Node(2)  # defining left child
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)  # defining right child
tree.root.right.right = Node(7)


#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))




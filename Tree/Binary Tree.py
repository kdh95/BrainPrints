class Node:
    def _init_(self, value = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def _init_(self):
        self.root = None


bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
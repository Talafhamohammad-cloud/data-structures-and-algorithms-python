class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class ktree:
    def __init__(self):
        self.root = None
    def preorder(self):
        self.values = []
        if self.root == None:
            return "empty tree"
        def ordering(node):
            self.values += [node.value]
            if node.left:
                ordering(node.left)
            if node.right:
                ordering(node.right)
            return self.values
        return ordering(self.root)
def fizz_buzz(ktree):
    if not ktree.root:
        return "empty tree"
    transformation = []
    def ordering(root):
        if root.value == None:
           return
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = "fizzbuzz"
        elif root.value % 3 == 0:
            root.value == "fizz"
        elif root.value % 5 == 0:
            root.value = "buzz"
        transformation.append(root.value)
        ordering(root.left)
        ordering(root.right)
        return transformation

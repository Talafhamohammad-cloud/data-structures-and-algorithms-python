
class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
###########################################################################################
class binarytree:
    def __init__(self):
        self.root = None
    def inorder(self):
            self.values = []
            if not self.root:
                return "empty tree"
            def ordering(node):
                if node.left:
                    ordering(node.left)
                self.values += [node.value]
                if node.right:
                    ordering(node.right)
                return self.values
            return ordering(self.root)
##################################################################################################
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
###################################################################################################
    def postorder(self):
            self.values = []
            if not self.root:
                return "empty tree"
            def ordering(node):
                if node.left:
                    ordering(node.left)
                if node.right:
                    ordering(node.right)
                self.values += [node.value]
                return self.values
            return ordering(self.root)
#######################################################(code challenge-16)########################
# ch-16 adding new method to find the max-value in numaric tree 
##################################################################################################
    def max_value(self):
          self.values = []
          if self.root == None:
                return "empty tree"
          def ordering(node):
                self.values += [node.value]
                if node.left:
                    ordering(node.left)
                if node.right:
                    ordering(node.right)
                return max(self.values)
          return ordering(self.root)
##################################################################################################
class binarysearchtree(binarytree):
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right
########################################################################################################
    def Contains(self, value):
        if self.root == None:
            return 'empty tree'
        else:
            current = self.root
            while current:
                if current.value == value:
                    return "the value is exist"
                elif value < current.value:
                    if current.left == None:
                        return "dose not exist"
                    current = current.left
                else:
                    if current.right == None:
                        return "dose not exist"
                    current = current.right
####################################################################
# Driver code "for quick test"
#if __name__ == '__main__':
#    tree = binarysearchtree()
#    tree.add(1)
#    tree.add(5)
#    tree.add(2)
#    tree.add(7)
#    tree.add(11)
#    tree.add(3)
#    tree2 =binarysearchtree()
#print(tree.inorder())
#print(tree.postorder())
#print(tree.preorder())
#print(tree.Contains(6))
#print(tree2.Contains(6))
####################################################################################################
# ch-16 adding 

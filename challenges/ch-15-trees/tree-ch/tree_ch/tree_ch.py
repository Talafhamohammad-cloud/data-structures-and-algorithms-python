
class Nodet:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Nodet(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            self.front.value
        except:
            return "Empty queue"
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value

    def isEmpty(self):
        if self.front == None and self.rear == None:
            return True
        else:
            return False
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
#######################################################(code challenge-17)###############################################
# ch-17 adding new method called breadth-first Return: list of all values in the tree, in the order they were encountered
#########################################################################################################################

    def breadth_first(self):
        if self.root == None:
            return "empty tree"
        else:
            queue = Queue()
            queue.enqueue(self.root)
            finalresult = []
            while queue != queue.isEmpty():
                front = queue.dequeue()
                finalresult.append(front.value)
                if front.left:
                    queue.enqueue(front.left)
                if front.right:
                    queue.enqueue(front.left)
        return finalresult
#########################################################################################################################        
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

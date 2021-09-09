class Nodetree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

##############################################################################################

class Binary_Tree:

    def __init__(self):
        self.root = None
    def pre_order(self):
        try:
            self.values = []

            if self.root == None:
                return "empty"

            def tree(node):
               self.values += [node.value]
               if node.left:
                   tree(node.left)
               if node.right:
                   tree(node.right)
               return self.values

            return tree(self.root)
        except:
            return "there is error"

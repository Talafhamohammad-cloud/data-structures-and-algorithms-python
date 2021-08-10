class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
###########################################################################        
class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        node = Node(value)
        if self.top == None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
    def pop(self):
        if not self.isEmpty():
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            return "empty stack"
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    def peek(self):
        try:
            return self.top.value
        except:
            return "empty stack"
################################################################################            
class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.secand_stack = Stack()
        self.rear = None
        self.front = None

    def enqueue(self, value):
        self.first_stack.push(value)
        self.rear = self.first_stack.top.value

    def dequeue(self):
        if self.first_stack.top:
            stack1 = self.first_stack
            while not stack1.isEmpty():
                self.secand_stack.push(stack1.pop())

            poped = self.secand_stack.pop()
            self.front = self.secand_stack.top
            self.first_stack = Stack()
            stack2 = self.secand_stack
            while not stack2.isEmpty():
                self.first_stack.push(stack2.pop())
            return poped

    def __str__(self):
        content = ''
        current = self.first_stack.top
        while current:
            content += f"{{{str(current.value)}}} -> "
            current = current.next
        content += " Null"
        return content
#####################################################################
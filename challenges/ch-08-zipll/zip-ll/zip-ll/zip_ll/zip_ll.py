class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, new_data: int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def zip(self, p, q):
        first = p.head
        second = q.head

        while first != None and second != None:
            fnext = first.next
            snext = second.next
            second.next = fnext  
            first.next = second 
            first = fnext
            second = snext
            q.head = second
    def __str__(self):
        output = ""
        crrval = self.head
        while crrval:
            data = crrval.data
            if crrval.next is None:
                output += f"( {data} ) -> None"
                break
            output = output + f"( {data} ) -> "
            crrval = crrval.next
        return output

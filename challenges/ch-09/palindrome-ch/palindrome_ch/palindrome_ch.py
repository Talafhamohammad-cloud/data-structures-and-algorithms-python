def palindrome(self):
    node = self.head
    length = 0
    comp = []
    while node:
      comp.append(node.data)
      node = node.next
      length += 1
    node = self.head
    for item in comp[::-1]:
      if (item!= node.data):
        return False 
      node = node.next
    return True
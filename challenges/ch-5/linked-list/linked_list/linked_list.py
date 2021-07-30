#########################################-NodeClass-#############
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
##########################-linkedlist class With its methods:-###
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value='null'):
        try:
          node = Node(value)
          if not self.head:
              self.head = node
          else:
              crrval = self.head
              self.head = node
              self.head.next = crrval
        except Exception as error:
          raise Exception(f"ooops!! : {error}")

    def append(self, value='null'):
        try:
          node = Node(value)
          if not self.head:
              self.head = node

          else:
              crrval = self.head
              while crrval.next != None:
                  crrval = crrval.next
              crrval.next = node
        except Exception as error:
          raise Exception(f"ooops!! : {error}")

    def content(self, n):
        try:
          x = False

          crrval = self.head
          while crrval:
              if crrval.value == n:

                  x = True
                  break
              crrval = crrval.next
          return x
        except Exception as error:
          raise Exception(f"ooops!! : {error}")

    def __str__(self):
        output = ""
        crrval = self.head
        while crrval:
            value = crrval.value
            if crrval.next is None:
                output += f"( {value} ) -> None"
                break
            output = output + f"( {value} ) -> "
            crrval = crrval.next
        return output



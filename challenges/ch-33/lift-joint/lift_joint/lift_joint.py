class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value='null'):
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

    def includes(self, n):
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
##################################################################################################
class Hashtable:
    def __init__(self, size=2048):
        self.size = size
        self.map = [None]*size
###############################################################

    def add(self, key, value):
        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key, value))
################################################################

    def get(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.map[hashed_key].head.data[0]
            current = self.map[hashed_key].head
            while current:
                if current.data[0] == key:
                    return current.data[1]
                else:
                    current = current.next
        return None
###############################################################
    def contains(self, key):
        
        idx_hash = self.hash(key)
        if self._buckets[idx_hash] == None:
            return False
        else:
            current = self._buckets[idx_hash].head
            if current == None:
                return False
            else:
                while current:
                    if list(current.value.keys())[0] == key:
                        return True
                    current = current.next
                return False
#####################################################################
    def hash(self, key):
      
        if type(key) == int:
            ASCII = key
        else:
            ASCII = sum([ord(char) for char in key])

        index = (ASCII*59) % self.size
        return index
########################################################################
    def __str__(self):

        for bucket in self._buckets:
            if bucket != None:
                self.str_bucket += bucket.__str__()

        return self.str_bucket
###########################################################################
def leftjoin(h1, h2):
    final_result = []
    if h1.map == h1.size*[None]:
        return 'Right is empty'
    if h2.map == h2.size*[None]:
        return 'left is empty'
    for item in h1.map:
        if item:
            a2=[]
            a2.append(item.head.data[0])
            a2.append(h1.get(item.head.data[0]))
            a2.append(h2.get(item.head.data[0]))
            final_result.append(a2)
    return final_result
#########################################################################
##################### strech Goal (Right joint) #########################
#########################################################################
def rightjoin(h1, h2):
    final_result = []
    if h1.map == h1.size*[None]:
        return 'Right is empty'
    if h2.map == h2.size*[None]:
        return 'left is empty'
    for item in h2.map:
        if item:
            a2 = []
            a2.append(item.head.data[0])
            a2.append(h2.get(item.head.data[0]))
            a2.append(h1.get(item.head.data[0]))
            final_result.append(a2)
    return final_result


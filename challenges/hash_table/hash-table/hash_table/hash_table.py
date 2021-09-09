class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
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
        self._buckets = [None]*self.size
        self.str_bucket = ''
###############################################################
    def add(self, key, value):
       
        index = self.hash(key)

        if self._buckets[index] == None:
           self._buckets[index] = LinkedList()

        self._buckets[index].append({key: value})
################################################################
    def get(self, key):
        
        index = self.hash(key)
        if self._buckets[index] == None:
            return "KEY DNE"
        else:
            if self._buckets[index].head == None:
                return "empty"
            else:
                current = self._buckets[index].head
                while current:
                    if list(current.value.keys())[0] == key:
                        return current.value[key]
                    current = current.next
                return "KEY DNE"
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

##################################################################################################################
def repeatedword(string):
    if not string:
        return "empty"
    strng =[".",",","-"]  
    for char in strng:  
     string = (string.replace(char, "")).lower()
    words = string.split()
    new_hashtable = Hashtable()
    for word in words:
        if new_hashtable.contains(word):
            return word
        else:
            new_hashtable.add(word, word)
    return "There is no duplication"
#########################################################################

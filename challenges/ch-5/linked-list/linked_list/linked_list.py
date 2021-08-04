#########################################-NodeClass-#############
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
##########################-linindexedlist class With its methods:-###


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
###########################################################################################ch-06#####
# tese methods to add insert before and insert after the append method i already added it in previos

    def insertbefore(self, value, new):
        crrval = self.head
        if crrval.value == value:
            self.insert(new)
        else:
          while crrval:
             if crrval.next.value == value:
                nextvalue = crrval.next
                crrval.next = Node(new)
                crrval.next.next = nextvalue
                break
             crrval = crrval.next

    def insertafter(self, value, new):
        crrval = self.head
        while crrval:
            if crrval.value == value:
                nextvalue = crrval.next
                crrval.next = Node(new)
                crrval.next.next = nextvalue
                break
            crrval = crrval.next
#########################################################-ch-07-##############################################
########### adding indexth method to find index-th value from the end of a linindexed list-###################

    def kth_method(self, index):
        crrval = self.head
        linklength = 1
        while crrval.next:
            linklength += 1
            crrval = crrval.next
        crrval = self.head
        if index >= linklength:
            return "Not In Range"
        elif index < 0:
            return "ooops!!! its negative"
        else:
            count = linklength-index-1
            for i in range(linklength):
                   if i == count:
                        return crrval.value
            crrval = crrval.next
###################################################-ch-08-##############################################################
########################### adding method to merge two linked list togother############################################
    def zip_Lists(self,first,second):
        f1=first.head
        f2=second.head
        f1.next=f2
        f1=f1.insertafter(f1.next,f2.next)
        




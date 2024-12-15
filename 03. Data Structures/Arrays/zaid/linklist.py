class linklist:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

def add(self, e):
    newNode = Node(e)
    newNode.next = self.__head
    self.head = newNode
    self.__size += 1
    if self.__tail == None:
      self.__tail = self.__head

class Node:
    def __init__(self, e):
      self.element = e
      self.next = None
    

def insert(self,index, e):
   if index == 0:
      self.addFirst(e)
   elif index >= self.__size:
      self.ddlist(e)
   else:
      current = self.__hade
      for i in range(1, index):
        current = current.next
      temp = current.next
      current.next = Node(e)  
      (current.next).next = temp
      self.__size += 1
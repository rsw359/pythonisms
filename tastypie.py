from threading import currentThread


class LinkedList:

  def __init__(self, collection= None):
    self.head = None
    if collection:
      for item in reversed(collection): #without reversed LL would be (c)>(b)>(a)
        self.insert(item)


# dunder iter makes the LL iterable, which also allows us to use len
  def __iter__(self):

    def val_gerator():

      current = self.head

      while current:

        yield current.value  

        current = current.next 

    return val_gerator()   

# dunder str allows us to get a string representation of our LL by append the values to an empty string
  def __str__(self):

        out = ""

        for value in self:
            out += f"[ {value} ] -> "

        return out + "None"

#dunder len allows us to get the length of the list after it has been made iterable and the iterable has been made into a list
  def __len__(self):
    return len(list(iter(self)))

#dunder eq allows us to evaluate whether two lists are the same
  def __eq__(self, other):
    return list(self) == list(other)
      

  def insert(self, value):
    self.head = Node(value, self.head)

  

  def append(self, value):
    node = Node(value)

    if not self.head:
      self.head = node
      return
    
    current = self.head
    
    while current:
      current = current.next

    current.next = node


class Node:
  def __init__(self, value, next_ = None):
    self.value = value
    self.next = next_
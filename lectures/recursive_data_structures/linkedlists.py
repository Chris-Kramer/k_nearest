from typing import Any, Optional

class LinkedList:
  """An implementation of lists based on the (singly) linked list. """

  # Each instance maintains a chain of elements using the inner class _Node
  # Each node in the chain stores a data element of the list and a reference
  # to the next node of the chain (or None if it's the last one).
  # The instance attribute _head maintains a pointer to the first node of the
  # chain or stores None if the list is empty.
  # The length of the list is stored in the instance attribute _length for
  # efficiency. This saves the need to traverse the chain every time one needs
  # to access the list length.
  
  class _Node:
    """ An inner class for the linked nodes forming the list.
    Each node stores an element of the list (attribute *data*)
    and a pointer the following node (attribute *next*).
    """
    def __init__(self, data, next=None):
      self.data = data
      self.next = next

    def __repr__(self):
      return f"Node({repr(self.data)},{self.next})"

  def __init__(self):
    self.clear()

  def __repr__(self):
      return 'LinkedList(' + ', '.join(repr(x) for x in self) + ')'
      # this alternative does not require __iter__, instead it proceeds
      # by recursion on the chain of nodes (see _Node.__repr__)
      # return f"LinkedList{repr(self.__head)}"
  
  def is_empty(self) -> bool:
    """ Whether the list is empty."""
    return self.__head is None

  def add(self, value):
    """ Adds data at the beginning of the list."""
    self.__head = LinkedList._Node(value,self.__head)
    self.__length += 1

  def clear(self):
    """Empties this list."""
    self.__head = None
    self.__length = 0

  # The following methods are invoked by Python to implement aspects of list-like
  # types such as lists. For more, see
  # https://docs.python.org/3/reference/datamodel.html#emulating-container-types

  def __len__(self) -> int:
    """ Returns the length of the list. This method is used by Python to
    implement the built-in function len."""
    return self.__length

  def __iter__(self):
    """ Returns an iterator for traversing the elements of this list."""
    node = self.__head
    while node is not None:
      yield node.data
      node = node.next

  def __getitem__(self,key):
    """Called to implement evaluation of self[key]."""
    # todo: support slices
    if isinstance(key,int):
      if -len(self) <= key < len(self):
        # if the index is negative we need to start from the end of the list
        # so we are looking for the element at length + key (key is negative)
        if key < 0:
          key += len(self)
        n = self.__head
        for _ in range(key):
          n = n.next
        return n.data
      else:
        raise IndexError("list index out of range")
    else:
      raise TypeError("list indices must be integers, not " + type(key).__name__)

  def __setitem__(self,key,value):
    """Called to implement assignment to self[key]."""
    if isinstance(key,int):
      if -len(self) <= key < len(self):
        # if the index is negative we need to start from the end of the list
        # so we are looking for the element at length + key (key is negative)
        if key < 0:
          key += len(self)
        n = self.__head
        for _ in range(key):
          n = n.next
        n.data = value
      else:
        raise IndexError("list index out of range")
    else:
      raise TypeError("list indices must be integers, not " + type(key).__name__)

  def __delitem__(self,key):
    """Called to implement deletion of self[key]."""
    if isinstance(key,int):
      if -len(self) <= key < len(self):
        if key < 0:
           key += len(self)
        if key == 0:
          self.__head = self.__head.next
        else:
          # find the predecessor of key
          n = self.__head
          for _ in range(key-1):
            n = n.next
          n.next = n.next.next
        self.__length -= 1
      else:
        raise IndexError("list index out of range")
    else:
      raise TypeError("list indices must be integers, not " + type(key).__name__)

  def __reversed__(self):
    """Called by the reversed()."""
    l = LinkedList()
    for x in self:
      l.add(x)
    return l

  def __contains__(self, item):
    """Called to implement membership test operators."""
    n = self.__head
    while n is not None and n.data is not item:
      n = n.next
    return n is not None
  
if __name__ == '__main__':
  l = LinkedList()
  print(l)
  l.add('a')
  l.add('b')
  print(l)
  assert l[-2] == l[0]
  print(reversed(l))
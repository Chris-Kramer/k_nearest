class BinaryTree:
  class _Node:
    def __init__(self,data,left=None,right=None):
      self.data = data
      self.left = left
      self.right = right
    def __repr__(self):
      return f"Node({repr(self.data)},{repr(self.left)},{repr(self.right)})"
  
  def __init__(self):
    self._root = None
  
  @staticmethod
  def _size(n):
    if n:
      return 1 + BinaryTree._size(n.left) + BinaryTree._size(n.right)
    else:
      return 0

  def size(self):
    return BinaryTree._size(self._root)

  def __len__(self):
    return self.size()
  
  def height(self):
    def h(n):
      if n:
        return 1 + max(h(n.left),h(n.right))
      else:
        return 0
    return h(self._root)

  def __str__(self):
    def f(n):
      if n:
        return f"({n.data},{f(n.left)},{f(n.right)})"
      else:
        return '()'
    return f(self._root)
  
  def __repr__(self):
    return f"BinaryTree({repr(self._root)})"

  def add(self,data):
    def a(n):
      if n:
        if BinaryTree._size(n.left) <= BinaryTree._size(n.right):
          n.left = a(n.left)
        else:
          n.right = a(n.right)
        assert 0 <= BinaryTree._size(n.left) - BinaryTree._size(n.right) <= 1 
        return n
      else:
        return BinaryTree._Node(data)
    self._root = a(self._root)
  
  def preorder(self):
    def f(n):
      if n:
        yield(n.data)
        yield from f(n.left)
        yield from f(n.right)
    yield from f(self._root)
  
  def inorder(self):
    def f(n):
      if n:
        yield from f(n.left)
        yield(n.data)
        yield from f(n.right)
    yield from f(self._root)

  def postorder(self):
    def f(n):
      if n:
        yield from f(n.left)
        yield from f(n.right)
        yield(n.data)
    yield from f(self._root)
  
  def __iter__(self):
    return self.preorder()

if __name__ == '__main__':
  print('### BinaryTree ###')
  t = BinaryTree()
  print(t)
  h = 4
  for x in range(2 ** h - 1):
    t.add(x)
    print('added',x,'size is', t.size(),'height is',t.height())
    #print(t)
  assert t.height() == h
  assert t.size() == 2 ** t.height() - 1

class BinarySearchTree(BinaryTree):
  def add(self,data):
    def a(n):
      if n:
        if data < n.data :
          n.left = a(n.left)
        else:
          n.right = a(n.right)
        return n
      else:
        return BinaryTree._Node(data)
    self._root = a(self._root)
  
  def __contains__(self,item):
    def f(n,l=0):
      # print('searching',item,'call depth',l)
      if n:
        if item == n.data:
          return True
        elif item < n.data:
          return f(n.left, l+1)
        else:
          return f(n.right, l+1)
    return f(self._root)

  """ an iterative variant
  def __contains__(self,item):
    n = self._root
    while n and n.data != item:
      if item < n.data:
        n = n.left
      else:
        n = n.right
    return n is not None
  """

if __name__ == '__main__':
  print('### BinarySearchTree ###')
  s = BinarySearchTree()
  for x in t.inorder():
    s.add(x)
    print('added',x,'size is', s.size(),'height is',s.height())
    #print(s)
  print(s)

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class binarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    newNode = Node(value)
    if self.root == None:
      self.root = newNode
      return

    current = self.root
    while True:
      if newNode.value < current.value:
        # LEFT
        if not current.left:
          current.left = newNode
          return
        current = current.left
      else:
        # RIGHT
        if not current.right:
          current.right = newNode
          return
        current = current.right
  
  def lookup(self, value):
    if not self.root:
      return False
    else:
      current = self.root
    
    while current:
      if current.value == value:
        return True, current.value
      elif value < current.value:
        current = current.left
      else:
        current = current.right
        # LEFT
    return False

  # def remove(self, value):
  #   if self.root == None:
  #     return print("Tree has no nodes")
  #   current = self.root
  #   parent = None
  #   while current:
  #     if value < current.value:
  #       parent = current
  #       current = current.left
  #     elif value > current.value:
  #       parent = current
  #       current = current.right
  #     elif current.value == value:
  #       # MATCH FOUND

  #       # OPTION 1: No Right Child
  #       if current.right == None:
  #         if parent == None:
  #           self.root = current.left
  #         else:
  #           # if parent > current value, make current left child a child of parent
  #           if current.value < parent.value:
  #             parent.left = current.left
  #           # if parent < current value, make left child a right child of parent
  #           elif current.value > parent.value:
  #             parent.right = current.left
        
  #       # OPTION 2 No Left Child
  #       if current.right.left == None:
  #         if parent == None:
  #           self.root = current.
tree = binarySearchTree()
tree.insert(9)
# tree.insert(4)
# tree.insert(6)
# tree.insert(5)
# tree.insert(7)
tree.remove(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# print(tree.lookup(15))

# REMOVE 38
          #     60
          #   /    \
          # 30    
          #  \
          #  54
          #  /\
          # 38 55
          #  \
          #  44         

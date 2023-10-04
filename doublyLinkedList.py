class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
  
  def append(self, data):
    newNode = Node(data)
    if self.head is None and self.tail is None:
      self.head = newNode
      self.tail = newNode
      self.length += 1
    else:
      newNode.prev = self.tail
      self.tail.next = newNode
      self.tail = newNode
      self.length += 1

  def prepend(self, data):
    newNode = Node(data)
    if self.head is None and self.tail is None:
      self.head = newNode
      self.tail = newNode
      self.length += 1
    else:
      self.head.prev = newNode
      newNode.next = self.head
      self.head = newNode
      self.length += 1

  # Lookup
  def traverseToIndex(self, index):
    #check index
    counter = 0
    currentNode = self.head
    while counter != index:
      currentNode = currentNode.next
      counter += 1
    return currentNode

  def insert(self, index, data):
    if index == 0:
      return self.prepend(data)
    elif index >= self.length:
      return self.append(data)
    
    newNode = Node(data)
    #Finding Nodes Left and Right of insert index
    leftNode = self.traverseToIndex(index-1)
    rightNode = leftNode.next
    #Updating pointers for leftNode and newNode
    leftNode.next = newNode
    newNode.next = rightNode

    newNode.prev = leftNode
    rightNode.prev = newNode
    self.length += 1
  
  def remove(self, index):
    leftNode = self.traverseToIndex(index-1)
    if index >= self.length:
      print("Out of LinkedList Bounds")
      return
    elif index == self.length - 1:
      leftNode.next = None
      self.length -= 1
    else:
      currentNode = leftNode.next
      rightNode = currentNode.next
      rightNode.prev = leftNode
      leftNode.next = currentNode.next
      self.length -= 1
    return
    # 10 -> 5 -> 16 -> 7 -> none
    # 10 -> 5 ->  X  -> 7 -> 2

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")
    print(self.length)

myLinkedList = DoublyLinkedList()
myLinkedList.append(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.append(10)
myLinkedList.prepend(5)
myLinkedList.prepend(16)
myLinkedList.append(2)
myLinkedList.prepend(2)
myLinkedList.insert(3, 13)
myLinkedList.remove(4)
myLinkedList.remove(7)
myLinkedList.remove(6)
myLinkedList.remove(6)
myLinkedList.display()
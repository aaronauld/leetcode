class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0
  
  def peek(self):
    if self.length == 0:
      return print("Queue Empty")
    else:
      return self.first.data

  def enqueue(self, value):
    newNode = Node(value)
    if self.length == 0:
      self.first = newNode
      self.last = newNode
      self.length += 1
    else:
      self.last.next = newNode
      self.last = newNode
      self.length += 1

  def dequeue(self):
    if self.length == 0:
      return print("no element to dequeue")
    elif self.first == self.last:
      self.last = None
    self.first = self.first.next
    self.length -= 1
    return
  
  def isEmpty(self):
    if self.length == 0:
      return print("Queue is empty")
    return print("Queue is of Size:",self.length)
  
  def display(self):
    current = self.first
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

myQueue = Queue()
myQueue.enqueue(3)
myQueue.enqueue(23)
print(myQueue.peek())
myQueue.enqueue(17)
myQueue.dequeue()
myQueue.isEmpty()
myQueue.display()
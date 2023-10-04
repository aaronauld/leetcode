class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    if self.length == 0:
      return "Stack Empty"
    else:
      return self.top.data
  
  def push(self,data):
    newNode = Node(data)
    if self.length == 0:
      self.top = newNode
      self.bottom = newNode
      self.length += 1
    else:
      temp = self.top
      self.top = newNode 
      self.top.next = temp
    self.length += 1
  
  def pop(self):
    if self.length == 0:
      return print("No elements to pop!")
    elif self.top == self.bottom:
      self.bottom = None
    self.top = self.top.next
    self.length -= 1

    return
  
  def isEmpty(self):
    if self.length == 0:
      return print("Stack is empty")
    return print("Stack is of Size:",self.length)

  def display(self):
    current = self.top
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")
  
myStack = Stack()
myStack.push("google")
myStack.push("udemy")
myStack.push("discord")
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.peek())
# myStack.pop()
# myStack.display()
# myStack.isEmpty()
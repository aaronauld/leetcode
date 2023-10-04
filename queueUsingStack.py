class MyQueue:
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self, data):
        self.first.append(data)

    def dequeue(self):
        self.peek()
        return self.last.pop()

    def peek(self):
        if not self.last:
            while self.first:
                self.last.append(self.first.pop())
        
        temp = self.last.pop()
        self.last.append(temp)
        return temp

    def empty(self):
        return not self.first and not self.last
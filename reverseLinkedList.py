def reverse(self):
  if self.length == 0:
    return print("LinkedList has no elements")
  else:
    prev = None
    curr = self.head
    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    

prev = 21
curr = None
next = None

# [5 -> 7 -> 13 -> 21 -> null]
# [null <- 5 <- 7 <- 13 <- 21]

# [null <- 5 -> 7 -> 13 ...]
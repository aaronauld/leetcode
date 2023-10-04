def recurring(array):
  seen = {}
  for key, element in enumerate(array):
    if element in seen:
      return element
    seen[element] = key
  return "no recurring"

# testing = [2,5,1,2,3,5,1,2,4]
# print(recurring(testing))

# testing = [2,1,1,5,6,3,6,4,3]
# print(recurring(testing))

testing = [2,3,4,5]
print(recurring(testing))


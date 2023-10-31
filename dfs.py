def dfsInOrder():

    return traverseInOrder(self.root, [])


def dfsPreOrder():

    return traversePreOrder(self.root, [])


def dfsPostOrder():

    return traversePostOrder(self.root, [])


#          9
#       4    20
#     1  6  15  170

def traverseInOrder(node, list):
    if node.left:
        traverseInOrder(node.left, list)
    list.append(node.value)
    if node.right:
        traverseInOrder(node.right, list)
    return list  # [1, 4, 6, 9, 15, 20, 170]


def traversePreOrder(node, list):
    list.append(node.value)
    if node.left:
        traversePreOrder(node.left, list)
    if node.right:
        traversePreOrder(node.right, list)
    return list  # [9, 4, 1, 6, 20, 15, 170]


def traversePostOrder(node, list):
    if node.left:
        traversePostOrder(node.left, list)
    if node.right:
        traversePostOrder(node.right, list)
    list.append(node.value)
    return list  # [1,6, 4, 15, 170, 20, 9]

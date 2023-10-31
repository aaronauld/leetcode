def bfs(visited, graph, node):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    queue.append(node)

    while queue:
        currentNode = queue.pop(0)
        visited.append(currentNode)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

    return visited


def bfsRecursive(queue, list):
    # base case
    if not queue:
        return list

    # Recursive case
    currentNode = queue.pop(0)
    list.append(currentNode)

    if currentNode.left:
        queue.append(currentNode.left)

    if currentNode.right:
        queue.append(currentNode.right)

    return self.bfsRecursive(queue, list)

# This is how you would use the recursive function.
# Example of Dynamic Programming, since the variables would get reset everytime otherwise
# .bfsRecursive(self.root, [])

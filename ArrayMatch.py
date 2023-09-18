# Example 1 - FALSE
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']


# Example 2 - TRUE
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'a']


# Brute Force (Approach 1)
def bruteMatch(input1, input2):
    for element1 in input1:
        for element2 in input2:
            if element1 == element2:
                return True
    return False


print(bruteMatch(array1, array2))

# Optimized (Approach 2)


def optimizeMatch(input1, input2):
    convertDict = {}
    # Loop through input1 and convert to a dictionary with {Value:Seen(boolean)}
    for element1 in input1:
        convertDict[element1] = True
    # Loop through input2 and check with dictionary
    for element2 in input2:
        if element2 in convertDict:
            return True

    return False


print(optimizeMatch(array1, array2))

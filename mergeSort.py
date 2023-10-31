import math


def mergeSort(array):
    if (len(array) <= 1):
        return array

    middle = math.floor(len(array)/2)
    left = array[:middle]
    right = array[middle:]

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    answer = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            answer.append(left[leftIndex])
            leftIndex += 1
        else:
            answer.append(right[rightIndex])
            rightIndex += 1
    print(answer)

    answer.extend(left[leftIndex:])
    answer.extend(right[rightIndex:])

    return answer


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
test = mergeSort(numbers)
print(test)

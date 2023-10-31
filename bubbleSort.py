def bubbleSort(array):
    for firstElement in range(len(array)):
        for secondElement in range(len(array)-1):
            if array[secondElement] > array[secondElement + 1]:
                temp = array[secondElement]
                array[secondElement] = array[secondElement + 1]
                array[secondElement + 1] = temp
    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(numbers)
print(bubbleSort(numbers))

def selectionSort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(numbers)
print(selectionSort(numbers))

def insertionSort(array):
    for i in range(1, len(array)):
        temp = array[i]

        j = i-1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = temp

    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(numbers)
print(insertionSort(numbers))

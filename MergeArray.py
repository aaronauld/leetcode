def MergeArray(array1, array2):
    mergedArray = []
    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if (array1[i] < array2[j]):
            mergedArray.append(array1[i])
            i += 1
        else:
            mergedArray.append(array2[j])
            j += 1

    while i < len(array1):
        mergedArray.append(array1[i])
        i += 1

    while j < len(array2):
        mergedArray.append(array2[j])
        j += 1

    return (mergedArray)


a = [0, 3, 4, 31]
b = [4, 6, 30]
print(MergeArray(a, b))

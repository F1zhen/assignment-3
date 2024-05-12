def selectionSort(array, size):
    for i in range(size):
        min = i

        for j in range(i + 1, size):
            if array[j] < array[min]:
                min_index = j
        (array[i], array[min]) = (array[min], array[i])



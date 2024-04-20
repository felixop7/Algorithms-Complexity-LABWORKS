def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

data = [1, 6, 2, 8, 3]
selectionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
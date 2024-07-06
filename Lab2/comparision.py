import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(15000)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

data_sizes = [1000, 2000, 3000, 4000, 5000]
best_times = {'quick': [], 'merge': [], 'insertion': [], 'selection': []}
worst_times = {'quick': [], 'merge': [], 'insertion': [], 'selection': []}

for size in data_sizes:
    best_case_data = list(range(size))
    worst_case_data = list(range(size, 0, -1))

    for algorithm in ['quick', 'merge', 'insertion', 'selection']:
        # Best case
        data_copy = best_case_data.copy()
        start_time = time.time()
        if algorithm == 'quick':
            quickSort(data_copy, 0, len(data_copy) - 1)
        elif algorithm == 'merge':
            mergeSort(data_copy)
        elif algorithm == 'insertion':
            insertionSort(data_copy)
        elif algorithm == 'selection':
            selectionSort(data_copy)
        best_times[algorithm].append(time.time() - start_time)

        # Worst case
        data_copy = worst_case_data.copy()
        start_time = time.time()
        if algorithm == 'quick':
            quickSort(data_copy, 0, len(data_copy) - 1)
        elif algorithm == 'merge':
            mergeSort(data_copy)
        elif algorithm == 'insertion':
            insertionSort(data_copy)
        elif algorithm == 'selection':
            selectionSort(data_copy)
        worst_times[algorithm].append(time.time() - start_time)

# Plotting the results
plt.figure(figsize=(12, 8))
for algorithm in ['quick', 'merge', 'insertion', 'selection']:
    plt.plot(data_sizes, best_times[algorithm], label=f'{algorithm.capitalize()} Sort Best Case')
    plt.plot(data_sizes, worst_times[algorithm], label=f'{algorithm.capitalize()} Sort Worst Case', linestyle='--')

plt.xlabel('Data Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Comparison of Sorting Algorithms (Best vs Worst Case)')
plt.legend()
plt.grid(True)
plt.show()

import random
import time
import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

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

    return arr

# Generate arrays and measure execution times
sizes = range(100, 10000)
best_times = []
worst_times = []

for size in sizes:
    # Best case (already sorted array)
    best_case_array = list(range(size))
    
    # Worst case (reverse sorted array)
    worst_case_array = list(range(size, 0, -1))

    # Measure time for best case
    start_time = time.time()
    mergeSort(best_case_array)
    end_time = time.time()
    best_times.append(end_time - start_time)
    
    # Measure time for worst case
    start_time = time.time()
    mergeSort(worst_case_array)
    end_time = time.time()
    worst_times.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, best_times, label='Best Case (Sorted)')
plt.plot(sizes, worst_times, label='Worst Case (Reverse Sorted)')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('MergeSort Execution Time Analysis for Best and Worst Cases')
plt.legend()
plt.grid(True)
plt.show()

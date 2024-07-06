import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)

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

# Generate arrays and measure execution times
sizes = range(100,1000)
best_times = []
worst_times = []

for size in sizes:
    # Best case (randomized)
    best_case_array = [random.randint(1, 1000) for _ in range(size)]
    random.shuffle(best_case_array)  # Ensuring random distribution

    # Worst case (already sorted)
    worst_case_array = sorted(best_case_array)

    # Measure time for best case
    start_time = time.time()
    quickSort(best_case_array, 0, len(best_case_array) - 1)
    end_time = time.time()
    best_times.append(end_time - start_time)
    
    # Measure time for worst case
    start_time = time.time()
    quickSort(worst_case_array, 0, len(worst_case_array) - 1)
    end_time = time.time()
    worst_times.append(end_time - start_time)

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(sizes, best_times, label='Best Case (Randomized)')
plt.plot(sizes, worst_times, label='Worst Case (Sorted)')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('QuickSort Execution Time Analysis for Best and Worst Cases')
plt.legend()
plt.grid(True)
plt.show()

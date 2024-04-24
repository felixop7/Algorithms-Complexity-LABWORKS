import time
import random
import matplotlib.pyplot as plt

def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

data_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
best_times = []
worst_times = []

for size in data_sizes:
    # Generate best case data (sorted array)
    data = [i for i in range(1, size + 1)]

    start_time = time.time()
    selectionSort(data)
    end_time = time.time()
    best_times.append(end_time - start_time)

    # Generate worst case data (reverse sorted array)
    data = [i for i in range(size, 0, -1)]

    start_time = time.time()
    selectionSort(data)
    end_time = time.time()
    worst_times.append(end_time - start_time)

plt.plot(data_sizes, best_times, label='Best Case')
plt.plot(data_sizes, worst_times, label='Worst Case')
plt.xlabel('Data Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Selection Sort Time Taken vs Data Size (Best and Worst Case)')
plt.legend()
plt.show()
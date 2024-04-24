import time
import random
import matplotlib.pyplot as plt

def insertionSort(array):
    """
    Sorts an array in place using the insertion sort algorithm.

    The outer loop iterates over each element in the array, starting with the second element.
    For each element, the inner loop shifts elements in the sorted portion of the array to the right
    until it finds the correct position for the current element. The current element is then inserted
    in its correct position.

    :param array: The array to be sorted
    :type array: list
    """
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

data_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
best_times = []
worst_times = []

for size in data_sizes:
    # Generate best case data (sorted array)
    data = [i for i in range(1, size + 1)]

    start_time = time.time()
    insertionSort(data)
    end_time = time.time()
    best_times.append(end_time - start_time)

    # Generate worst case data (reverse sorted array)
    data = [i for i in range(size, 0, -1)]

    start_time = time.time()
    insertionSort(data)
    end_time = time.time()
    worst_times.append(end_time - start_time)

plt.plot(data_sizes, best_times, label='Best Case')
plt.plot(data_sizes, worst_times, label='Worst Case')
plt.xlabel('Data Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Insertion Sort Time Taken vs Data Size (Best and Worst Case)')
plt.legend()
plt.show()
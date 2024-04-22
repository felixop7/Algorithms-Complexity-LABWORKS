import time
import random
import matplotlib.pyplot as plt

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

data_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
insertion_times = []
selection_times = []

for size in data_sizes:
    data = [random.randint(1, size) for _ in range(size)]

    start_time = time.time()
    insertionSort(data)
    end_time = time.time()
    insertion_times.append(end_time - start_time)

    start_time = time.time()
    selectionSort(data)
    end_time = time.time()
    selection_times.append(end_time - start_time)

plt.plot(data_sizes, insertion_times, label='Insertion Sort')
plt.plot(data_sizes, selection_times, label='Selection Sort')
plt.xlabel('Data Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Insertion Sort vs Selection Sort Time Taken vs Data Size')
plt.legend()
plt.show()
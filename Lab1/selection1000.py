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

data_sizes = [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
times = []

for size in data_sizes:
    data = [random.randint(1, size) for _ in range(size)]
    start_time = time.time()
    selectionSort(data)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(data_sizes, times)
plt.xlabel('Data Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Selection Sort Time Taken vs Data Size')
plt.show()
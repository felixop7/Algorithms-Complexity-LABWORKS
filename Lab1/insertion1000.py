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

data_sizes = [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
times = []

for size in data_sizes:
    data = [random.randint(1, size) for _ in range(size)]
    start_time = time.time()
    insertionSort(data)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(data_sizes, times)
plt.xlabel('Data Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Insertion Sort Time Taken vs Data Size')
plt.show()
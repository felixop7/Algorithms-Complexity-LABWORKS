import matplotlib.pyplot as plt
import random
import time

def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Choose a random pivot index within the range
    pivot = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move the pivot element to the end
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    stack = []
    stack.append((low, high))
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def best_case_time_complexity(n):
    # Best case: When the pivot element always divides the array into equal halves
    arr = [i for i in range(n)]
    start_time = time.perf_counter()
    quicksort(arr, 0, n-1)
    end_time = time.perf_counter()
    return end_time - start_time

def worst_case_time_complexity(n):
    # Worst case: When the pivot element always divides the array into one element and the rest of the array
    arr = [i for i in range(n, 0, -1)]
    start_time = time.perf_counter()
    quicksort(arr, 0, n-1)
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == "__main__":
    # Generating random input sizes
    sizes = list(range(0, 10001, 100))
    random.shuffle(sizes)  # Shuffle the list to randomize input sizes

    # Calculate time complexities
    best_times = [best_case_time_complexity(size) for size in sizes]
    worst_times = [worst_case_time_complexity(size) for size in sizes]

    # Plotting
    plt.plot(sizes, best_times, label='Best Case Time Complexity')
    plt.plot(sizes, worst_times, label='Worst Case Time Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort Time Complexity Analysis')
    plt.legend()
    plt.show()

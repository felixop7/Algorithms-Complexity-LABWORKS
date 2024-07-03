def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    for j in range(low, high):
        if arr[j] <= pivot:
            # Swap elements at index i and j
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the position of the pivot
    return i + 1

# Test array
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)

print("Sorted array is:", arr)
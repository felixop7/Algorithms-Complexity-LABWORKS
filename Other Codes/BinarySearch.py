def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(sorted_list, 9))  # Output: 4
print(binary_search(sorted_list, 20))  # Output: -1

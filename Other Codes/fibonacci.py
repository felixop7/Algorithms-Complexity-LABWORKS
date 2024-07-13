def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            next_term = fib_series[-1] + fib_series[-2]
            fib_series.append(next_term)
        return fib_series

# Example usage
print(fibonacci(0))  # Output: []
print(fibonacci(1))  # Output: [0]
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

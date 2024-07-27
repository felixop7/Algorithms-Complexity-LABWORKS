def matrix_chain_multiplication(dims):
    n = len(dims) - 1  # Number of matrices
    
    # Initialize a 2D array to store the minimum cost
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a 2D array to store the optimal split point
    split_point = [[0] * n for _ in range(n)]
    
    # Build the solution bottom-up
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split_point[i][j] = k
    
    # Print the optimal order of matrix multiplications up to A1 to A4
    def print_optimal_order(i, j):
        if i == j:
            if i <= 3:
                print(f"A{i}", end="")
            else:
                return
        else:
            print("(", end="")
            print_optimal_order(i, split_point[i][j])
            print(" x ", end="")
            print_optimal_order(split_point[i][j] + 1, j)
            print(")", end="")
    
    print("Optimal order of matrix multiplications up to A1 to A4:")
    print_optimal_order(0, 3)
    print()
    
    return dp[0][n - 1]

# Example usage
dimensions = [30, 35, 15, 5, 10, 20, 25]
minimum_cost = matrix_chain_multiplication(dimensions)
print("Minimum number of scalar multiplications:", minimum_cost)

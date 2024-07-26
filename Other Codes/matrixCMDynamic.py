def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1  # Number of matrices
    
    # Create a 2D table to store the minimum cost
    dp = [[0] * n for _ in range(n)]
    
    # Fill the table bottom-up
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1])
    
    return dp[0][n - 1]

# Example usage
dimensions = [30, 35, 15, 5, 10, 20, 25]
minimum_cost = matrix_chain_multiplication(dimensions)
print("Minimum number of scalar multiplications:", minimum_cost)





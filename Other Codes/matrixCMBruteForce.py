def matrix_chain_multiplication_brute_force(dims, i, j):
    if i == j:
        return 0
    
    min_cost = float('inf')
    for k in range(i, j):
        cost = matrix_chain_multiplication_brute_force(dims, i, k) + \
              matrix_chain_multiplication_brute_force(dims, k + 1, j) + \
              dims[i] * dims[k + 1] * dims[j + 1]
        min_cost = min(min_cost, cost)
    
    return min_cost

# Example usage
dimensions = [30, 35, 15, 5, 10]
minimum_cost = matrix_chain_multiplication_brute_force(dimensions, 0, len(dimensions) - 2)
print("Minimum number of scalar multiplications:", minimum_cost)

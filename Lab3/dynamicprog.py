def knapsack_dynamic(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

val = [80, 100, 120]
wt = [10, 20, 30]
W = 45
n = len(val)
print("Maximum value in 0/1 knapsack using Dynamic method: ", knapsack_dynamic(W, wt, val, n))

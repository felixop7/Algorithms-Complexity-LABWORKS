def bruteforce_knapsack(p, w, m):
    assert len(p) == len(w), "p and w differ"

    n = len(p)
    max_profit = 0
    total_weight = m
    soln = ''
    combinations = []

    for i in range(2**n):
        s = bin(i)[2:].rjust(n, '0')
        profit = sum((int(s[j])) * p[j] for j in range(n))
        weight = sum((int(s[j])) * w[j] for j in range(n))
        
        combinations.append((s, weight, profit))
        
        if profit > max_profit and weight <= total_weight:
            max_profit = profit
            soln = s

    # Print the table of all combinations
    print(f"{'Combination':>15} {'Weight':>10} {'Profit':>10}")
    for comb in combinations:
        print(f"{comb[0]:>15} {comb[1]:>10} {comb[2]:>10}")

    print("\nBest choice is:", soln)
    print("Maximum profit is:", max_profit)

    return max_profit

p = [80, 100, 120]
w = [10, 20, 30]
m = 45

bruteforce_knapsack(p, w, m)

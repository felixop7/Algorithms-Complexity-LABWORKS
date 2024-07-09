def greedy_knapsack(values, weights, capacity):
    assert len(values) == len(weights), "values and weights differ"

    n = len(values)
    items = list(range(n))
    # Sort the items in descending order of their value/weight ratio
    items.sort(key=lambda i: values[i] / weights[i], reverse=True)

    total_weight = 0
    max_profit = 0
    combinations = []

    for i in items:
        if total_weight + weights[i] <= capacity:
            total_weight += weights[i]
            max_profit += values[i]
            combinations.append((weights[i], values[i], total_weight, max_profit))
        else:
            remaining_weight = capacity - total_weight
            fraction = remaining_weight / weights[i]
            max_profit += values[i] * fraction
            total_weight += weights[i] * fraction
            combinations.append((weights[i] * fraction, values[i] * fraction, total_weight, max_profit))
            break

    # Print the table of all combinations
    print(f"{'Weight Added':>15} {'Value Added':>15} {'Total Weight':>15} {'Total Profit':>15}")
    for comb in combinations:
        print(f"{comb[0]:>15.2f} {comb[1]:>15.2f} {comb[2]:>15.2f} {comb[3]:>15.2f}")

    print("\nMaximum profit is:", max_profit)

    return max_profit

# Example usage
values = [80, 100, 120]
weights = [10, 20, 30]
capacity = 45

greedy_knapsack(values, weights, capacity)

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(values, weights, capacity):
    # Create a list of items with their value, weight, and value-to-weight ratio
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Total value of items in the knapsack
    for item in items:
        if capacity >= item.weight:
            # If the item can be fully added, add it
            capacity -= item.weight
            total_value += item.value
        else:
            # If the item can't be fully added, add the fractional part
            total_value += item.value * (capacity / item.weight)
            break  # Knapsack is full

    return total_value

# Example usage
values = [80, 100, 120]
weights = [10, 20, 30]
capacity = 45

max_profit = fractional_knapsack(values, weights, capacity)
print("Maximum profit is:", max_profit)

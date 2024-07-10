import unittest
from bruteforce_knapsack import bruteforce_knapsack
from dynamicprog import knapsack_dynamic
from fractionalBruteforce import fractional_knapsack
from fractionalGreedy import greedy_knapsack

class KnapsackTest(unittest.TestCase):
    
    def test_bruteforce_knapsack(self):
        p = [280, 100, 120, 120]
        w = [40, 10, 20, 24]
        m = 60
        expected_output = 400
        result = bruteforce_knapsack(p, w, m)
        self.assertEqual(result, expected_output)

    def test_knapsack_dynamic(self):
        val = [20, 5, 10, 40, 15, 25]
        wt = [1, 2, 3, 8, 7, 4]
        W = 10
        n = len(val)
        expected_output = 60
        result = knapsack_dynamic(W, wt, val, n)
        self.assertEqual(result, expected_output)

    def test_fractional_knapsack(self):
        values = [280, 100, 120, 120]
        weights = [40, 10, 20, 24]
        capacity = 60
        expected_output = 440.0
        result = fractional_knapsack(values, weights, capacity)
        self.assertEqual(result, expected_output)

    def test_greedy_knapsack(self):
        values = [280, 100, 120, 120]
        weights = [40, 10, 20, 24]
        capacity = 60
        expected_output = 440.0
        result = greedy_knapsack(values, weights, capacity)
        self.assertEqual(result, expected_output)
    
if __name__ == "__main__":
    unittest.main()

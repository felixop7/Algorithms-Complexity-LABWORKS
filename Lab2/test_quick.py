import unittest
from quick import quickSort

class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        # Initialize the input data as a list of integers
        input_data = [10, 7, 8, 9, 1, 5]
        
        # Call the quickSort function with the input data as an argument
        quickSort(input_data, 0, len(input_data) - 1)
        
        # Assert that the sorted input data is equal to the expected output
        self.assertEqual(input_data, [1, 5, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()

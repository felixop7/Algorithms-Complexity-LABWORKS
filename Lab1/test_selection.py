import unittest
from selection import selectionSort

class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        # Initialize the input data as a list of integers
        input_data = [1, 6, 2, 8, 3]
        
        # Call the selectionSort function with the input data as an argument
        selectionSort(input_data)
        
        # Assert that the sorted input data is equal to the expected output
        self.assertEqual(input_data, [1, 2, 3, 6, 8])

if __name__ == '__main__':
    unittest.main()
import unittest
from merge import mergeSort

class TestQuickSort(unittest.TestCase):

    def test_merge_sort(self):
        # Initialize the input data as a list of integers
        input_data = [10, 7, 8, 9, 1, 5]
        
        # Call the quickSort function with the input data as an argument
        mergeSort(input_data)
        
        # Assert that the sorted input data is equal to the expected output
        self.assertEqual(input_data, [1, 5, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()

import unittest
import time
from random import randint
from Sorts.Heapsort import heapSort, heapify
from Sorts.Insertionsort import insertionSort
from Sorts.Mergesort import mergeSort, merge
from Sorts.Quicksort import partition, quickSort
from Sorts.Selectionsort import selectionSort


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.sizes = [1000, 5000, 10000]

        self.data_types = {
            "random": lambda size: [randint(0, 10000) for i in range(size)],
            "sorted": lambda size: list(range(size)),
            "reverse_sorted": lambda size: list(range(size - 1, -1, -1)),
            "identical": lambda size: [5] * size
        }

    def test_performance(self):
        for size in self.sizes:
            for data_type, data_generator in self.data_types.items():
                print(f"\nTesting with {data_type} data of size {size}:")
                arr = data_generator(size)

                self._test_sort(heapSort, arr.copy(), "Heap Sort")
                self._test_sort(selectionSort, arr.copy(), "Selection Sort", size)
                self._test_sort(insertionSort, arr.copy(), "Insertion Sort")
                self._test_sort(mergeSort, arr.copy(), "Merge Sort", 0, len(arr) - 1)
                self._test_sort(quickSort, arr.copy(), "Quick Sort", 0, len(arr) - 1)

    def _test_sort(self, sort_function, arr, sort_name, *args):
        start_time = time.time()
        sort_function(arr, *args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{sort_name}: {elapsed_time:.6f} seconds")



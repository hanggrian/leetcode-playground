import unittest
from typing import override

from src.problems1.median_of_two_sorted_array import SOLUTIONS
from tests.testing.sampled_test import SampledTest


class TestMedianOfTwoSortedArrays(SampledTest):
    @override
    def get_file_name(self) -> str:
        return 'median_of_two_sorted_arrays.json'

    def test(self):
        for solution in SOLUTIONS:
            for sample in self.get_samples():
                self.assertEqual(
                    sample['output'],
                    solution.find_median_sorted_arrays(
                        sample['input']['nums1'],
                        sample['input']['nums2'],
                    ),
                    sample['explanation'],
                )


if __name__ == '__main__':
    unittest.main()

import unittest
from src import ch04

class Ch02Tests(unittest.TestCase):
  def test_sum(self):
    test_params = [
      ([0, 1, 2, 3, 4], 10),
      ([1, -3, 0.5, -0.2], -1.7)
    ]

    for target_list, expected in test_params:
      with self.subTest(arr=target_list):
        self.assertAlmostEqual(ch04.sum(target_list), expected)
  
  def test_quickSort(self):
    test_params = [
      ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]),
      ([1, -3, 0.5, -0.2], [-3, -0.2, 0.5, 1]),
      ([3, 2, 1, 3, 2, 1], [1, 1, 2, 2, 3, 3])
    ]

    for target_list, expected in test_params:
      with self.subTest(arr=target_list):
        self.assertEqual(ch04.quickSort(target_list), expected)

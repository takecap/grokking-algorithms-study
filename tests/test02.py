import unittest
from src import ch02

class Ch02Tests(unittest.TestCase):
  def test_findSmallest(self):
    test_params = [
      ([0, 1, 2, 3, 4], 0),
      ([1, -3, 0.3, -0.2], 1)
    ]

    for target_list, expected in test_params:
      with self.subTest(arr=target_list):
        self.assertEqual(ch02.findSmallest(target_list), expected)

  def test_selectionSort(self):
    test_params = [
      ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]),
      ([1, -3, 0.3, -0.2], [-3, -0.2, 0.3, 1])
    ]
    for target_list, expected in test_params:
      with self.subTest(arr=target_list):
        self.assertEqual(ch02.selectionSort(target_list), expected)

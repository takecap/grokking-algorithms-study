import unittest
from src import ch01

class Ch01Tests(unittest.TestCase):
  def test_binary_search(self):
    test_patterns = [
      ([0, 1, 2, 3, 5, 8], 5, 4),
      ([0, 1, 2, 3, 5, 8], 10, None)
    ]

    for target_list, target_item, expected in test_patterns:
      with self.subTest(sorted_list=target_list, item=target_item):
        self.assertEqual(ch01.binarySearch(target_list, target_item), expected)

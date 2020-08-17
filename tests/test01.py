import unittest
from src import ch01

class Ch01Tests(unittest.TestCase):
  def test_binary_search(self):
    my_list = [0, 1, 2, 3, 5, 8]
    expected = 4
    actual = ch01.binarySearch(my_list, 5)
    self.assertEqual(expected, actual)

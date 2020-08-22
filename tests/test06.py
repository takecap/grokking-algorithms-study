import unittest
from src import ch06

class Ch06Tests(unittest.TestCase):
  def test_searchMangoSeller(self):
    test_params = [
      ('you', True),
      ('bob', False),
      ('claire', True)
    ]

    for target, expected in test_params:
      with self.subTest(name=target):
        self.assertEqual(ch06.searchMangoSeller(target), expected)

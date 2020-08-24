import unittest
from src import ch06

class Ch06Tests(unittest.TestCase):
  def test_searchMangoSeller(self):
    friends_graph = ch06.friends_graph
    test_params = [
      ('you', friends_graph, True),
      ('bob', friends_graph, False),
      ('claire', friends_graph, True),
      ('claire', { 'claire': ['meary', 'henrym'], 'meary': [], 'henrym': [] }, True)
    ]

    for target, graph, expected in test_params:
      with self.subTest(name=target):
        self.assertEqual(ch06.searchMangoSeller(target, graph), expected)

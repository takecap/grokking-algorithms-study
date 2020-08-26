import unittest
from src import ch07

graph_piano = {
  'start': {'lp': 5, 'poster': 0},
  'lp': {'base': 15, 'drum': 20},
  'poster': {'base': 30, 'drum': 35},
  'base': {'piano': 20},
  'drum': {'piano': 10},
  'piano': {}
}
graph_A = {
  'start': {'a': 5, 'b': 2},
  'a': {'c': 4, 'd': 2},
  'b': {'a': 8, 'd': 7},
  'c': {'finish': 3, 'd': 6},
  'd': {'finish': 1},
  'finish': {}
}
graph_B = {
  'start': {'a': 10},
  'a': {'b': 20},
  'b': {'c': 1, 'finish': 30},
  'c': {'a': 1},
  'finish': {}
}

class Ch07Tests(unittest.TestCase):
  def test_findLowestCostNode(self):
    costs, _ = ch07.init_tables(graph_piano)
    costs1 = costs.copy()
    costs1['base'], costs1['drum'] = 20, 25
    test_params = [
      (costs, [], 'poster'),
      (costs, ['poster'], 'lp'),
      (costs1, ['poster', 'lp'], 'base')
    ]
    for table, processed, expected in test_params:
      with self.subTest(costs=table, processed=processed):
        self.assertEqual(ch07.findLowestCostNode(table, processed), expected)
  
  def test_searchDijkstra(self):
    infinity = float('inf')
    return infinity

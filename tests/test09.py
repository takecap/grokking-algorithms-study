import unittest
from src import ch09

class Ch09Tests(unittest.TestCase):
  def test_solveKnapsackProblem(self):
    test_params = [
      ({'guitar': (1500, 1), 'stereo': (3000, 4), 'laptop': (2000, 3)}, 4, 1, {'guitar', 'laptop'}),
      ({'guitar': (1500, 1), 'stereo': (3000, 4), 'laptop': (2000, 3), 'iphone': (2000, 1)}, 4, 1, {'iphone', 'laptop'}),
      ({'wm': (7, 0.5), 'gt': (6, 0.5), 'ng': (9, 1), 'bm': (9, 2), 'cc': (8, 0.5)}, 2, 0.5, {'wm', 'ng', 'cc'})
    ]
    
    for items, capa, unit, expected in test_params:
      with self.subTest(items=items, capacity=capa, unit=unit):
        self.assertEqual(ch09.solveKnapsackProblem(items, capa, unit), expected)

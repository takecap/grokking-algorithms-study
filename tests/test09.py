import unittest
from src import ch09

class Ch09Tests(unittest.TestCase):
  def test_solveKnapsackProblem(self):
    test_params = [
      ({'guitar': (1500, 1), 'stereo': (3000, 4), 'laptop': (2000, 3)}, 4, 1, {'guitar', 'laptop'}),
      ({'guitar': (1500, 1), 'stereo': (3000, 4), 'laptop': (2000, 3), 'iphone': (2000, 1)}, 4, 1, {'iphone', 'laptop'}),
      ({'wm': (7, 0.5), 'gt': (6, 0.5), 'ng': (9, 1), 'bm': (9, 2), 'cc': (8, 0.5)}, 2, 0.5, {'wm', 'ng', 'cc'}),
      (
        {'guitar': (1500, 1), 'stereo': (3000, 4), 'laptop': (2000, 3), 'iphone': (2000, 1), 'mp3': (1000, 1)},
        4, 1, {'iphone', 'guitar', 'mp3'}
      ),
      (
        {'water': (10, 3), 'book': (3, 1), 'food': (9, 2), 'jacket': (5, 2), 'camera': (6, 1)},
        6, 1, {'food', 'camera', 'water'}
      )
    ]
    
    for items, capa, unit, expected in test_params:
      with self.subTest(items=items, capacity=capa, unit=unit):
        self.assertEqual(ch09.solveKnapsackProblem(items, capa, unit), expected)
  
  def test_solveLCSubsequence(self):
    test_params = [
      ('fosh', 'fish', 3),
      ('fosh', 'fort', 2),
      ('blue', 'clues', 3)
    ]
    
    for str1, str2, expected in test_params:
      with self.subTest(string1=str1, string2=str2):
        self.assertEqual(ch09.solveLCSubsequence(str1, str2), expected)

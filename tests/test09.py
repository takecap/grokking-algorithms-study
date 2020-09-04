import unittest
from src import ch09

class Ch09Tests(unittest.TestCase):
  def test_solveKnapsackProblem(self):
    test_params = []
    for items, capa, expected in test_params:
      with self.subTest(items=itesm, capacity=capa):
        self.assertEqual(ch09.solveKnapsackProblem(items, capa), expected)

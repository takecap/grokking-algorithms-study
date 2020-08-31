import unittest
from src import ch08

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
station_list = {
  "kone": {"id", "nv", "ut"},
  "ktwo": {"wa", "id", "mt"},
  "kthree": {"or", "nv", "ca"},
  "kfour": {"nv", "ut"},
  "kfive": {"ca", "az"}
}

class Ch08Tests(unittest.TestCase):
  def test_greedySetCover(self):
    test_params = [(states_needed, station_list, {"kone", "ktwo", "kthree", "kfive"})]
    for states, stations, expected in test_params:
      with self.subTest(states=states, stations=stations):
        self.assertEqual(ch08.greedySetCover(states, stations), expected)

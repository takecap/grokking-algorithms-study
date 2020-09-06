def solveKnapsackProblem(items, capacity, unit=1):
  max_factor = int(capacity / unit)
  key_list = list(items.keys())
  values = [[set() for i in range(max_factor + 1)] for j in range(len(key_list) + 1)]
  return values[len(key_list)][max_factor]

def evalValue(items, itemSet):
  return sum([items[key][0] for key in itemSet])

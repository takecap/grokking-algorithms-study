import copy

def solveKnapsackProblem(items, capacity, unit=1):
  max_factor = int(capacity / unit)
  key_list = list(items.keys())
  item_set = [[set() for i in range(max_factor + 1)] for j in range(len(key_list) + 1)]

  for j, key in enumerate(key_list):
    for i in range(1, max_factor + 1):
      value, weight = items[key]
      weight = round(weight / unit)
      item_set[j + 1][i] = copy.copy(item_set[j][i])
      if i >= weight and evalValue(items, item_set[j][i]) < evalValue(items, item_set[j][i - weight]) + value:
        item_set[j + 1][i] = copy.copy(item_set[j][i - weight])
        item_set[j + 1][i].add(key)
#    print(item_set[j + 1])
  return item_set[len(key_list)][max_factor]

def evalValue(items, itemSet):
  return sum([items[key][0] for key in itemSet])

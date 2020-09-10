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

def solveLCSubsequence(string1, string2):
  str1 = string1.lower()
  str2 = string2.lower()
  grid = [[0 for i in string1] for j in string2]
  for i, ch1 in enumerate(str1):
    for j, ch2 in enumerate(str2):
      if i == 0 and j == 0:
        grid[j][i] = 1 if ch1 == ch2 else 0
      elif j == 0:
        if ch1 == ch2:
          grid[j][i] = 1
        else:
          grid[j][i] = grid[j][i - 1]
      elif i == 0:
        if ch1 == ch2:
          grid[j][i] = 1
        else:
          grid[j][i] = grid[j - 1][i]
      else:
        if ch1 == ch2:
          grid[j][i] = grid[j - 1][i - 1] + 1
        else:
          grid[j][i] = max(grid[j][i - 1], grid[j - 1][i])
  return grid[j][i]

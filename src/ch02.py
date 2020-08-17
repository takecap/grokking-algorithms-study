from copy import copy

def findSmallest(arr):
  smallest = arr[0]
  index = 0
  for idx in range(1, len(arr)):
    if arr[idx] < smallest:
      smallest = arr[idx]
      index = idx
  return index

def selectionSort(arr):
  orgArr = copy(arr)
  newArr = []
  for _ in range(len(arr)):
    idx = findSmallest(orgArr)
    newArr.append(orgArr.pop(idx))
  return newArr

def findSmallest(arr):
  smallest = arr[0]
  index = 0
  for idx in range(1, len(arr)):
    if arr[idx] < smallest:
      smallest = arr[idx]
      index = idx
  return index

def selectionSort(arr):
  newArr = []
  for _ in range(len(arr)):
    idx = findSmallest(arr)
    newArr.append(arr.pop(idx))
  return newArr

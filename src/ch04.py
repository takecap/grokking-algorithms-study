def sum(arr):
  if len(arr) == 0:
    return 0
  else:
    return arr[0] + sum(arr[1:])

def quickSort(arr):
  if len(arr) < 2:
    return arr
  pivot = arr[0]
  small = [num for num in arr[1:] if num < pivot]
  large = [num for num in arr[1:] if num >= pivot]
  return quickSort(small) + [pivot] + quickSort(large)

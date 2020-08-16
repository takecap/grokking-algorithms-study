def binarySearch(sorted_list, item):
  low, high = 0, len(sorted_list) - 1
  while low <= high:
    mid = (low + high) // 2
    guess = sorted_list[mid]
    if guess > item:
      high = mid - 1
    elif guess < item:
      low = mid + 1
    else:
      return mid
  return None

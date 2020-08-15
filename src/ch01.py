import time
def binary_search(sorted_list, item):
  low, high = 0, len(sorted_list) - 1
  while low <= high:
    mid = (low + high) // 2
    guess = sorted_list[mid]
    time.sleep(1)
    print(low, mid, high)
    if guess > item:
      high = mid - 1
    elif guess < item:
      low = mid + 1
    else:
      return mid
  return None

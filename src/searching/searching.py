# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(len(arr)):
    if target == arr[i]:
      return i

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
# def binary_search_recursive2(arr, target, low, high):
  
#   middle = (low+high)//2

#   if len(arr) == 0:
#     return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

def binary_search_recursive(arr, target, idx=0):
  if len(arr) == 0:
    return -1 # empty array
  
  if len(arr) == 1:
    if arr[0] is not target:
      return -1
    return idx
  
  mid = len(arr) // 2

  if arr[mid] == target:
    return idx + mid

  next_arr = arr[:mid] if arr[mid] > target else arr[mid:]

  if arr[mid] > target:
    next_arr = arr[:mid]
  else:
    next_arr = arr[mid:]
    idx = mid + idx

  return binary_search_recursive(next_arr, target, idx)

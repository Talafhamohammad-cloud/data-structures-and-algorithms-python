#vtos = value to search
array=[1,2,3,4,5,6,7,8,9]
def BinarySearch(array, vtos):
  lower = 0
  upper = len(array) - 1

  while lower <= upper:
    middle = lower+ (upper - lower) // 2
    if array[middle] == vtos:
      return middle
    elif array[middle] < vtos:
      lower = middle + 1
    else:
      upper = middle - 1
  return -1
print(BinarySearch(array,5))
print(BinarySearch(array, 7))
print(BinarySearch(array, 10))
print(BinarySearch(array, 1))


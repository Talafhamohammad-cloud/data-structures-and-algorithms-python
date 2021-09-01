arr1 = [8, 4, 23, 42, 16, 15]
arr2 = [20, 18, 12, 8, 5, -2]
arr3 = [5, 12, 7, 5, 5, 7]
arr4 = [2, 3, 5, 7, 13, 11]

def partition(array, low, high):
  pivot = array[high]

  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

print("###############################################################")
print("orginal array")
print(arr1)
size = len(arr1)
quickSort(arr1, 0, size - 1)
print('sorted array:')
print(arr1)
print("###############################################################")
print("orginal array")
print(arr2)
size = len(arr2)
quickSort(arr2, 0, size - 1)
print('sorted array:')
print(arr2)
print("###############################################################")
print("orginal array")
print(arr3)
size = len(arr3)
quickSort(arr3, 0, size - 1)
print('sorted array:')
print(arr3)
print("###############################################################")
print("orginal array")
print(arr4)
size = len(arr4)
quickSort(arr4, 0, size - 1)
print('sorted array:')
print(arr4)
print("###############################################################")


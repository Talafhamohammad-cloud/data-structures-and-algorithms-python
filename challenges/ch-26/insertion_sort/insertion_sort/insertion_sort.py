arr1 = [8, 4, 23, 42, 16, 15]
arr2 = [20, 18, 12, 8, 5, -2]
arr3 = [5, 12, 7, 5, 5, 7]
arr4 = [2, 3, 5, 7, 13, 11]
def insertion(arr):
    for i in range(len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp
    return arr

print("#######################################################\n")
print(f'insertion sort of Sample Array is: {insertion(arr1)}\n')
print(f'insertion sort of Reverse-sorted is: {insertion(arr2)}\n')
print(f'insertion sort of Few uniques is: {insertion(arr3)}\n')
print(f'insertion sort of Nearly-sorted is: {insertion(arr4)}\n')
print("#######################################################")

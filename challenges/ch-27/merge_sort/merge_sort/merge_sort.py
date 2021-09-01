arr1 = [8, 4, 23, 42, 16, 15]
arr2 = [20, 18, 12, 8, 5, -2]
arr3 = [5, 12, 7, 5, 5, 7]
arr4 = [2, 3, 5, 7, 13, 11]


def mergesort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergesort(L)
        mergesort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

mergesort(arr1)
mergesort(arr2)
mergesort(arr3)
mergesort(arr4)


print("###############################################")
print("Sorted arr1 is: ")
print(arr1)
print("###############################################")
print("Sorted arr2 is: ")
print(arr2)
print("###############################################")
print("Sorted arr3 is: ")
print(arr3)
print("###############################################")
print("Sorted arr4 is: ")
print(arr4)
print("###############################################")

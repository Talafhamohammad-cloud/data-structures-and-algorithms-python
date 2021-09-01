from quick_sort import __version__
from quick_sort.quick_sort import *

def test_version():
    assert __version__ == '0.1.0'
############################################################################
def test_insertion_sort():
    arr1 = [8, 4, 23, 42, 16, 15]
    size = len(arr1)
    quickSort(arr1,0,size-1)
    assert arr1 == [4, 8, 15, 16, 23, 42]


def test_reverse():
    arr2 = [20, 18, 12, 8, 5, -2]
    size = len(arr2)
    quickSort(arr2, 0, size-1)
    assert arr2 == [-2, 5, 8, 12, 18, 20]


def test_few_uniques():
    arr3 = [5, 12, 7, 5, 5, 7]
    size = len(arr3)
    quickSort(arr3, 0, size-1)
    assert arr3 == [5, 5, 5, 7, 7, 12]


def test_nearly_sorted():
    arr4 = [2, 3, 5, 7, 13, 11]
    size = len(arr4)
    quickSort(arr4, 0, size-1)
    assert arr4 == [2, 3, 5, 7, 11, 13]
##########################################################################

from insertion_sort.insertion_sort.insertion_sort import __version__
from insertion_sort.insertion_sort.insertion_sort import *

def test_version():
    assert __version__ == '0.1.0'
###############################################################


def test_insertion_sort():
    arr1 = [8, 4, 23, 42, 16, 15]
    actual = insertion(arr1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_reverse():
    arr2 = [20, 18, 12, 8, 5, -2]
    actual = insertion(arr2)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_few_uniques():
    arr3 = [5, 12, 7, 5, 5, 7]
    actual = insertion(arr3)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_nearly_sorted():
    arr4 = [2, 3, 5, 7, 13, 11]
    actual = insertion(arr4)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

from linked_list import __version__
from linked_list.linked_list import (LinkedList,)


def test_version():
    assert __version__ == '0.1.0'
################################-empty linked list-#############################################


def test_instantiate_empty_linked_list():
    empty = LinkedList()
    empty.append()
    actual = empty.__str__()
    expected = '( null ) -> None'
    assert actual == expected
###############################-insert to the head-################################################


def test_insert():
    insert = LinkedList()
    insert.append(1)
    insert.insert(2)
    actual = insert.head.value
    expected = 2
    assert actual == expected
###############################-point to the head-##################################################


def test_head_value():
    first = LinkedList()
    first.insert(2)
    actual = first.head.value
    expected = 2
    assert actual == expected
###############################-insert multiple-##################################################


def test_insert_and_head_value():
    multi = LinkedList()
    multi.insert('go')
    multi.insert('we')
    multi.insert('here')
    actual = multi.__str__()
    expected = '( here ) -> ( we ) -> ( go ) -> None'
    assert actual == expected
###############################-return true-######################################################


def test_includes_True():
    find = LinkedList()
    find.append(9)
    find.append(8)
    find.append(7)
    find.append(6)
    find.append(5)
    find.append(4)
    actual = find.includes(7)
    expected = True
    assert actual == expected
################################-return false-#####################################################


def test_includeses_False():
    dne = LinkedList()
    dne.append('mohammad')
    dne.append('khaled')
    dne.append('talafha')
    actual = dne.includes(11)
    expected = False
    assert actual == expected
##################################-all values-######################################################


def test_return_all_values():
    allv = LinkedList()
    allv.append('my')
    allv.append('name')
    allv.append('is:')
    actual = allv.__str__()
    expected = '( my ) -> ( name ) -> ( is: ) -> None'
    assert actual == expected

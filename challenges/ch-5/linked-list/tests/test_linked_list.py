from linked_list import __version__
from linked_list.linked_list import LinkedList


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
def test_includes_False():
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
################################-insert-before-head-#######################################################
def test_insert_before():
    before = LinkedList()
    before.append(1)
    before.append(2)
    before.append(3)
    before.insertbefore(1, 5)

    actual = before.__str__()
    expected = '( 5 ) -> ( 1 ) -> ( 2 ) -> ( 3 ) -> None'
    assert actual == expected
##################################-insert-after-head-########################################################
def test_insert_after():
    after = LinkedList()
    after.append(0)
    after.append(1)
    after.append(2)
    after.insertafter(0, 5)

    actual = after.__str__()
    expected = '( 0 ) -> ( 5 ) -> ( 1 ) -> ( 2 ) -> None'
    assert actual == expected
########################################-insert-after-the-end-#####################################################
def test_after_end():
    afend = LinkedList()
    afend.insert(1)
    afend.insert(2)
    afend.append(3)
    actual = afend.__str__()
    expected = '( 2 ) -> ( 1 ) -> ( 3 ) -> None'
    assert actual == expected
####################################-insert-before-middle-##################################################
def test_before_middle():
    bemid = LinkedList()
    bemid.append(1)
    bemid.append(2)
    bemid.append(3)
    bemid.insertbefore(2, 'added')
    actual = bemid.__str__()
    expected = '( 1 ) -> ( added ) -> ( 2 ) -> ( 3 ) -> None'
    assert actual == expected
###################################-insert-after-middle-##################################################
def test_before_middle():
    afmid = LinkedList()
    afmid.append(1)
    afmid.append(2)
    afmid.append(3)
    afmid.insertafter(2, 'added')
    actual = afmid.__str__()
    expected = '( 1 ) -> ( 2 ) -> ( added ) -> ( 3 ) -> None'
    assert actual == expected
##################################-insert-multi-after-end################################################
def test_multi_to_the_end():
    mend = LinkedList()
    mend.insert(1)
    mend.insert(2)
    mend.append(5)
    mend.append(4)
    mend.append(3)
    actual = mend.__str__()
    expected = '( 2 ) -> ( 1 ) -> ( 5 ) -> ( 4 ) -> ( 3 ) -> None'
    assert actual == expected

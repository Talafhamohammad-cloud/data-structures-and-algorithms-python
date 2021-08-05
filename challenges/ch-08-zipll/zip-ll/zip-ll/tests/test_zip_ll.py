from zip_ll import __version__
from zip_ll.zip_ll import LinkedList


def test_version():
    assert __version__ == '0.1.0'

################################## both of them are not empty #######################################
def test_twoll():
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.insert(1)      
    llist1.insert(2)
    llist1.insert(3) 
    llist2.insert(6)
    llist2.insert(7)
    llist2.insert(8)
    llist1.zip(p=llist1, q=llist2)
    actual = llist1.__str__()
    expected = '( 3 ) -> ( 8 ) -> ( 2 ) -> ( 7 ) -> ( 1 ) -> ( 6 ) -> None'
    assert actual == expected
############################ one of them is empty ############################################
def test_twoll_one_empty():
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.insert(1)
    llist1.insert(2)
    llist1.insert(3)
    llist1.insert(4)
    llist1.zip(p=llist1, q=llist2)
    actual = llist1.__str__()
    expected = '( 4 ) -> ( 3 ) -> ( 2 ) -> ( 1 ) -> None'
    assert actual == expected
################################## two of them are empty ###########################################
def test_twoll_two_empty():
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.zip(p=llist1, q=llist2)
    actual = llist1.__str__()
    expected = ''
    assert actual == expected
#################################################################################################

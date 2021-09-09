from hash_table import __version__
from hash_table.hash_table import *
from hash_table.btree import *
from hash_table.intersection import *
def test_version():
    assert __version__ == '0.1.0'
##############################################################
def test_hash_table_Adding_a_key_value():
    hashtable = Hashtable()
    hashtable.add('name', 'Mohammad')
    hash = hashtable.hash('name')
    actual = hashtable._buckets[hash].head.value
    expected = {'name': 'Mohammad'}
    assert actual == expected
##############################################################
def test_Retrieving_based_on_a_key_returns_the_value_stored():
    hashtable = Hashtable()
    hashtable.add('name', 'Mohammad')
    actual = hashtable.get('name')
    expected = 'Mohammad'
    assert actual == expected
#############################################################
def test_contains_True():
    hashtable = Hashtable()
    hashtable.add('last_name', 'Khaled')
    actual = hashtable.contains('last_name')
    expected = True
    assert actual == expected
##############################################################
def test_contains_False():
    hashtable = Hashtable()
    actual = hashtable.contains('last_name')
    expected = False
    assert actual == expected
#############################################################    
def test_collision():
    hashtable = Hashtable()
    hashtable.add('name', 'Mohammad')
    hashtable.add('last_name', 'Khaled')
    actual = hashtable.get('last_name')
    expected = 'Khaled'
    assert actual == expected
###############################################################
def test_hash_index():
    hashtable = Hashtable()
    actual = hashtable.hash('last_name')
    expected = 636
    assert actual == expected
##############################################################
######################## TEST REPEATED WORDS #################
##############################################################
def test_empty():
    string = ''
    actual = repeatedword(string)
    expected = 'empty'
    assert actual == expected
#########################################################
def test_one():
    string = "Once upon a time, there was a brave princess who"
    actual = repeatedword(string)
    expected = "a"
    assert actual == expected
############################################################
def test_two():
    string = "It was the best of times, it was the worst of times," 
    actual = repeatedword(string)
    expected = "it"
    assert actual == expected
#############################################################
def test_three():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York"
    actual = repeatedword(string)
    expected = "summer"
    assert actual == expected
################################################################
def test_four():
    string = "Hello from the other side "
    actual = repeatedword(string)
    expected = "There is no duplication"
    assert actual == expected

##############################################################
######################## TEST TREE INTERSECTION ##############
##############################################################
def test_empty():
    t1 = Binary_Tree()
    t2 = Binary_Tree()
    actual = tree_intersection(t1, t2)
    expected = "there is empty one or both of them"
    assert actual == expected
##########################################################################
def test_intersection():
    t1 = Binary_Tree()
    t1.root = Nodetree(1)
    t1.root.left = Nodetree(2)
    t1.root.right = Nodetree(3)
    t1.root.left.left = Nodetree(4)
    t1.root.left.right = Nodetree(5)
    t2 = Binary_Tree()
    t2.root = Nodetree(3)
    t2.root.left = Nodetree(4)
    t2.root.right = Nodetree(5)
    t2.root.left.left = Nodetree(7)
    t2.root.left.right = Nodetree(9)
    actual = tree_intersection(t1, t2)
    expected = [3,4,5]
    assert actual == expected
###########################################################################
##########################################################################
######################## TEST LIFT JOINT #################################
##########################################################################


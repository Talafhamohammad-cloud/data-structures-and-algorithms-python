from hash_table import __version__
from hash_table.hash_table import *

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
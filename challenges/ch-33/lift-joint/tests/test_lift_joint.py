from lift_joint import __version__
from lift_joint.lift_joint import *
import pytest
def test_version():
    assert __version__ == '0.1.0'
##################################################################################################################
def test_one(hash3, hash2):
    assert leftjoin(hash3, hash2) == 'Right is empty'

def test_two(hash1, hash3):
    assert leftjoin(hash1, hash3) == 'left is empty'

def test_three(hash1, hash2):
    assert leftjoin(hash1, hash2) == [['mohammad', 'first', 'first name'], ['ahmad', 'grand ', 'grandfather'], 
    ['talafha', 'family', 'family name'], ['khaled', 'second', ' second name']]


def test_four_rightjoint(hash1, hash2):
    assert rightjoin(hash1, hash2) == [['mohammad', 'first name', 'first'], ['ahmad', 'grandfather', 'grand '], 
    ['talafha', 'family name', 'family'], ['khaled', ' second name', 'second']]

######################################################################################################################    
@pytest.fixture
def hash3():
    h3 = Hashtable()
    return h3 
@pytest.fixture
def hash1():
    h1 = Hashtable()
    h1.add('mohammad', 'first')
    h1.add('khaled', 'second')
    h1.add('ahmad', 'grand ')
    h1.add('talafha', 'family')
    return h1
@pytest.fixture
def hash2():
    h2 = Hashtable()
    h2.add('mohammad', 'first name')
    h2.add('khaled', ' second name')
    h2.add('ahmad', 'grandfather')
    h2.add('talafha', 'family name')
    return h2

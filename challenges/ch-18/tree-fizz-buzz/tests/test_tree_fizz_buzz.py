from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import *

def test_version():
    assert __version__ == '0.1.0'
############################################################################# Test if its empty
def test_empty_tree():
    tree = ktree()
    assert fizz_buzz(tree) == "empty tree"



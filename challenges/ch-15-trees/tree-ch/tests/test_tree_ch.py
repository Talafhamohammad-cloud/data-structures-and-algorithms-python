from tree_ch import __version__
from tree_ch.tree_ch import binarysearchtree

def test_version():
    assert __version__ == '0.1.0'
######################################################################################
# first test "successfully instantiate an empty tree"
def test_empty_tree():
    tree = binarysearchtree()
    actual = tree.root
    expected = None
    assert actual == expected
#######################################################################################
# second test "successfully instantiate a tree with a single root node"
def test_single_root_node():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    actual = tree.root.value
    expected = 1
    assert actual == expected
########################################################################################
# third test "successfully add a left child and right child to a single root node"
def test_left_and_right_single_root_node():
    tree = binarysearchtree()
    tree.add(10)
    tree.add(2)
    tree.add(30)
    actual = (tree.root.left.value, tree.root.right.value)
    expected = (2,30)
    assert actual == expected
###########################################################################################
# fourth test "successfully return a collection from an inorder traversal"
def test_inorder_traversal():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(11)
    tree.add(3)
    actual = tree.inorder()
    expected = [1, 2, 3, 5, 7, 11]
    assert actual == expected
###########################################################################################
# fifth test "successfully return a collection from a preorder traversal"
def test_preorder_traversal():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(11)
    tree.add(3)
    actual = tree.preorder()
    expected = [1, 5, 2, 3, 7, 11]
    assert actual == expected
##########################################################################################
# sixth test "successfully return a collection from a postorder traversal"
def test_postorder_traversal():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(11)
    tree.add(3)
    actual = tree.postorder()
    expected = [3, 2, 11, 7, 5, 1]
    assert actual == expected
############################################################################################
# extra test "successfully return the value "dose not exist" in the tree "
def test_value_dne():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(11)
    tree.add(3)
    actual = tree.Contains(4)
    expected = "dose not exist"
    assert actual == expected
################################################################################################
# extra test "successfully return if the valeu exist in the tree "
def test_value_exist():
    tree = binarysearchtree()
    tree.add(1)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(11)
    tree.add(3)
    actual = tree.Contains(11)
    expected = "the value is exist"
    assert actual == expected
#################################################################################################
from graph_imp import __version__
from graph_imp.graph_imp import *

def test_version():
    assert __version__ == '0.1.0'
#########################################################################
def test_add_vertex():
    G = Graph()
    G.add_vertex('0')
    assert G.add_vertex('0').value == '0'
####################################################################
def test_add_edge():
    G = Graph()
    one = G.add_vertex('1')
    two = G.add_vertex('2')
    G.add_edge(one, two, 1)
    assert G.adjacency_list[one][0].vertix == two
########################################################################
def test_get_nodes():
    G = Graph()
    G.add_vertex('1')
    G.add_vertex('2')
    G.add_vertex('3')
    G.add_vertex('4')
    assert G.get_vertices() == ['1', '2', '3', '4']
#########################################################################
def test_get_neighbors():
    G = Graph()
    one = G.add_vertex('1')
    two = G.add_vertex('2')
    three = G.add_vertex('3')
    four = G.add_vertex('4')
    G.add_edge(one, two, 4)
    G.add_edge(one, four, 9)
    G.add_edge(one, three, 3)
    assert G.get_neighbors(one) == [('2', 4), ('4', 9), ('3', 3)]
#############################################################################
def test_size():
    G = Graph()
    G.add_vertex('0')
    G.add_vertex('1')
    G.add_vertex('2')
    G.add_vertex('3')
    G.add_vertex('4')
    G.add_vertex('5')
    assert G.size() == 6
################################################################################
def test_size_empty():
    G = Graph()
    actual = G.size()
    expected = 0
    assert actual == expected
################################################################################
def test_empty():
    G = Graph()
    assert G.get_vertices() == "null"
################################################################################
def test_graph_with_one_vertex():
    G = Graph()
    one = G.add_vertex('1')
    G.add_edge(one, one, 1)
    assert G.get_neighbors(one) == [('1', 1)]
##############################################################################

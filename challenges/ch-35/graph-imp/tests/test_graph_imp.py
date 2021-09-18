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
##############################################################################
########### code challenge-36 (graph-breadth-first)###########################
#################### (TEST) ##################################################
def test_breadth_one():
    G = Graph()
    a = G.add_vertex('mohammad')
    b = G.add_vertex('khaled')
    c = G.add_vertex('ahmad')
    d = G.add_vertex('fayad')
    e = G.add_vertex('Talafha')
    G.add_edge(a, a)
    G.add_edge(a, b)
    G.add_edge(a, d)
    G.add_edge(a, c)
    G.add_edge(b, a)
    G.add_edge(b, d)
    G.add_edge(b, c)
    G.add_edge(c, a)
    G.add_edge(c, d)
    G.add_edge(d, a)
    G.add_edge(d, b)
    G.add_edge(d, e)
    G.add_edge(d, c)
    assert G.breadthfirst(a) == ['mohammad', 'khaled', 'fayad', 'ahmad', 'Talafha']
#############################################################
def test_breadth_two():
    G = Graph()
    a = G.add_vertex('mohammad')
    b = G.add_vertex('khaled')
    c = G.add_vertex('ahmad')
    d = G.add_vertex('fayad')
    e = G.add_vertex('Talafha')
    f = G.add_vertex('name')
    G.add_edge(a, a)
    G.add_edge(a, d)
    G.add_edge(a, c)
    G.add_edge(b, a)
    G.add_edge(c, a)
    G.add_edge(c, d)
    G.add_edge(d, a)
    G.add_edge(d, b)
    G.add_edge(d, e)
    assert G.breadthfirst(f) == 'verteix has no adjecent'
#######################################################################
def test_breadth_three():
    G = Graph()
    a = G.add_vertex('mohammad')
    b = G.add_vertex('khaled')
    c = G.add_vertex('ahmad')
    d = G.add_vertex('fayad')
    e = G.add_vertex('Talafha')
    f = G.add_vertex('name')
    G.add_edge(a, a)
    G.add_edge(a, d)
    G.add_edge(a, c)
    G.add_edge(b, a)
    G.add_edge(c, a)
    G.add_edge(c, d)
    G.add_edge(d, a)
    G.add_edge(d, b)
    G.add_edge(d, e)
    assert G.breadthfirst("s") == 'vertix DNE in Graph'
###################################################################################
"""
test the stretch goals for breadth first if there is bath between two vertices or not
the story behind my implementation take the neighbors of the first vertix and then find the breadth fo each 
vertix in adjacency array if the second vertex belong to that array then there is path between them if not 
there is no path between them.  
"""
###################################################################################
def test_breadth_four():
    G = Graph()
    a = G.add_vertex('mohammad')
    b = G.add_vertex('khaled')
    c = G.add_vertex('ahmad')
    d = G.add_vertex('fayad')
    e = G.add_vertex('Talafha')
    G.add_edge(a, d)
    G.add_edge(a, c)
    G.add_edge(c, a)
    G.add_edge(b, d)
    G.add_edge(d, e)
    assert G.path_existance(a, e) == 'there is path between them'
##################################################################################
def test_breadth_five():
    G = Graph()
    a = G.add_vertex('mohammad')
    b = G.add_vertex('khaled')
    c = G.add_vertex('ahmad')
    d = G.add_vertex('fayad')
    e = G.add_vertex('Talafha')
    f = G.add_vertex('isolated')
    G.add_edge(a, d)
    G.add_edge(a, c)
    G.add_edge(c, a)
    G.add_edge(b, d)
    G.add_edge(d, e)
    G.add_edge(f, f)
    assert G.path_existance(a, f) == 'there is no path between them'

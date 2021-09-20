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

#######################################################################
########### code challenge-37 (graph-business-trip)####################
#######################################################################
def test_trip_one():
    G4 = Graph()
    pandora = G4.add_vertex('pandora')
    arendelle = G4.add_vertex('arendelle')
    metroville = G4.add_vertex('metroville')
    narina = G4.add_vertex('narina')
    naboo = G4.add_vertex('naboo')
    manstropolis = G4.add_vertex('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert businesstrip(G4, [naboo, pandora]) == "False,$0"
########################################################################
def test_trip_two():
    G4 = Graph()
    pandora = G4.add_vertex('pandora')
    arendelle = G4.add_vertex('arendelle')
    metroville = G4.add_vertex('metroville')
    narina = G4.add_vertex('narina')
    naboo = G4.add_vertex('naboo')
    manstropolis = G4.add_vertex('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert businesstrip(G4, [pandora, arendelle, metroville]) == "True,$249"
####################################################################################
def test_trip_three():
    G4 = Graph()
    pandora = G4.add_vertex('pandora')
    arendelle = G4.add_vertex('arendelle')
    metroville = G4.add_vertex('metroville')
    narina = G4.add_vertex('narina')
    naboo = G4.add_vertex('naboo')
    manstropolis = G4.add_vertex('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert businesstrip(G4, [pandora, metroville]) == "True,$82"
######################################################################################
#######################################################################
########### code challenge-38 (graph-depth-first)#####################
#######################################################################
def test_depth_one():
    G4 = Graph()
    pandora = G4.add_vertex('pandora')
    arendelle = G4.add_vertex('arendelle')
    metroville = G4.add_vertex('metroville')
    narina = G4.add_vertex('narina')
    naboo = G4.add_vertex('naboo')
    manstropolis = G4.add_vertex('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert G4.depthfirst(pandora) == ['pandora', 'arendelle', 'metroville', 'manstropolis', 'naboo', 'narina']
##################################################################################################################
def test_depth_two():
    G3 = Graph()
    a = G3.add_vertex('mohammad')
    b = G3.add_vertex('khaled')
    c = G3.add_vertex('ahmad')
    d = G3.add_vertex('fayad')
    e = G3.add_vertex('Talafha')
    f = G3.add_vertex('name')
    G3.add_edge(a, d)
    G3.add_edge(a, c)
    G3.add_edge(c, a)
    G3.add_edge(b, d)
    G3.add_edge(d, b)
    G3.add_edge(d, e)
    assert G3.depthfirst(a) == ['mohammad', 'fayad', 'khaled', 'Talafha', 'ahmad']
#######################################################################################################################
def test_depth_three():
    G3 = Graph()
    a = G3.add_vertex('mohammad')
    b = G3.add_vertex('khaled')
    c = G3.add_vertex('ahmad')
    d = G3.add_vertex('fayad')
    e = G3.add_vertex('Talafha')
    f = G3.add_vertex('name')
    G3.add_edge(a, d)
    G3.add_edge(a, c)
    G3.add_edge(c, a)
    G3.add_edge(b, d)
    G3.add_edge(d, b)
    G3.add_edge(d, e)
    assert G3.depthfirst(f) == 'verteix has no adjecent'
##################################################################################################################


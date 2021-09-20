import networkx as nx
import matplotlib.pyplot as plt
#######################################################################


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.front == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        try:
            self.front.value
        except:
            return "Empty queue"
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
#############################################################################


class Vertix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'V-{self.value}'


class Edge:
    def __init__(self, vertix, weight):
        self.vertix = vertix
        self.weight = weight


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.visual = []

    def add_vertex(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v

    def add_edge(self, v1, v2, weight=0):
        temp = [v1, v2]
        if v1 and v2 in self.adjacency_list:
            self.adjacency_list[v1].append(Edge(v2, weight))
        self.visual.append(temp)

    def get_vertices(self):
        if self.adjacency_list:
            return [key.value for key in self.adjacency_list]
        else:
            return 'null'

    def get_neighbors(self, vertix):
        return [(edge.vertix.value, edge.weight) for edge in self.adjacency_list[vertix]]

    def size(self):
        return len(self.adjacency_list)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
########################################################################
########### code challenge-36 (graph-breadth-first)####################
#######################################################################
    def breadthfirst(self, vertix):
        if vertix not in self.adjacency_list:
            return 'vertix DNE in Graph'
        elif self.adjacency_list[vertix] == []:
            return 'verteix has no adjecent'
        breadth = Queue()
        visited = []
        vertices = []
        breadth.enqueue(vertix)
        visited.append(vertix)

        while breadth.front:
            front = breadth.dequeue()
            vertices.append(front.value)

            for child in self.adjacency_list[front]:

                if child.vertix not in visited:
                    visited.append(child.vertix)
                    breadth.enqueue(child.vertix)

        return vertices
######################################################################
####################### (stretch goals for breadth first)#############
######################################################################
    def path_existance(self, vertex1, vertex2):
        """
        test the strech goals for breadth first if there is bath between two vertices or not
        the story behind my implementation take the neighbors of the first vertix and then find the breadth fo each 
        vertix in adjacency array if the second vertex belong to that array then there is path between them if not 
        there is no path between them.

        """
        adjarr=[]
        adjecency_v1 = self.adjacency_list[vertex1]
        for i in adjecency_v1:
            adjarr.append(i.vertix.value)
            adjecency_v2 = self.breadthfirst(i.vertix)
            for j in adjecency_v2:
                adjarr.append(j)         
        for vertex in adjarr:
            if vertex2.value not in adjarr:
                return "there is no path between them"
            else :
                return "there is path between them"
#######################################################################
########### code challenge-38 (graph-depth-first)#####################
#######################################################################
    def depthfirst(self, v):
        finalresult = []
        finalresult.append(v.value)
        if v not in self.adjacency_list:
            return 'vertix DNE in Graph'
        elif self.adjacency_list[v] == []:
            return 'verteix has no adjecent'
        def trail(v):
            neighbors = self.adjacency_list[v]
            for edge in neighbors:
                vertices = edge.vertix.value

                if vertices not in finalresult:
                    finalresult.append(vertices)
                    trail(edge.vertix)
        trail(v)
        return finalresult
#######################################################################
########### code challenge-37 (graph-business-trip)####################
#######################################################################
def businesstrip(Graph,array):
    path1 = False
    path2 = False
    total = 0
    for vertix in range(len(array) - 1):
        adjacency = Graph.adjacency_list[array[vertix]]
        path2 = False
        for edges in adjacency:
            if array[vertix + 1] == edges.vertix:
                total += edges.weight
                path1 = True
                path2 = True
    path = path1 and path2
    if not path:
        total = 0
        path = False
        return f'{path},${total}'
    return f'{path},${total}'
#######################################################################
if __name__ == "__main__":
    G = Graph()
    a=G.add_vertex('0')
    b=G.add_vertex('1')
    c=G.add_vertex('2')
    d=G.add_vertex('3')
    e=G.add_vertex('4')
    f=G.add_vertex('5')
    G.add_edge(0, 2)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(5, 3)
    G.add_edge(3, 4)
    G.add_edge(1, 0)
    ################
    G2 = Graph()
    pandora = G2.add_vertex('Pandora')
    arendelle = G2.add_vertex('Arendelle')
    metroville = G2.add_vertex('Metroville')
    monstroplolis = G2.add_vertex('Monstroplolis')
    narnia = G2.add_vertex('Narnia')
    naboo = G2.add_vertex('Naboo')
    n = G2.add_vertex('Na')
    G2.add_edge(pandora, arendelle, 1)
    G2.add_edge(arendelle, metroville, 1)
    G2.add_edge(arendelle, monstroplolis, 1)
    G2.add_edge(metroville, arendelle, 1)
    G2.add_edge(metroville, pandora, 1)
    G2.add_edge(metroville, monstroplolis, 1)
    G2.add_edge(metroville, narnia, 1)
    G2.add_edge(metroville, naboo, 1)
    G2.add_edge(monstroplolis, arendelle, 1)
    G2.add_edge(monstroplolis, metroville, 1)
    G2.add_edge(monstroplolis, arendelle, 1)
    G2.add_edge(narnia, metroville, 1)
    G2.add_edge(narnia, naboo, 1)
    G2.add_edge(naboo, monstroplolis, 1)
    G2.add_edge(naboo, metroville, 1)
    G2.add_edge(naboo, narnia, 1)
    ################
    G3 = Graph()
    a = G3.add_vertex('mohammad')
    b = G3.add_vertex('khaled')
    c = G3.add_vertex('ahmad')
    d = G3.add_vertex('fayad')
    e = G3.add_vertex('Talafha')
    f =G3.add_vertex('name')
    G3.add_edge(a, d)
    G3.add_edge(a, c)
    G3.add_edge(c, a)
    G3.add_edge(b, d)
    G3.add_edge(d, b)
    G3.add_edge(d, e)
    #####################################
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
    #######################################################
    #print(G2.breadthfirst(naboo))
    #print(G3.path_existance(a, b))
    print(G4.depthfirst(narina))

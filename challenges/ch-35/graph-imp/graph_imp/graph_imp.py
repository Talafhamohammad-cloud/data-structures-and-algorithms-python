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
####################### (stretch goals for breadth first)##############
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
######################################################################
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
    #print(G2.breadthfirst(naboo))
    print(G3.path_existance(a, b))

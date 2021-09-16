import networkx as nx
import matplotlib.pyplot as plt
#############################################################################
class Vertix:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'V-{self.value}'
class Edge:
    def __init__(self, vertix , weight):
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
if __name__ == "__main__":
    G = Graph()
    G.add_vertex('0')
    G.add_vertex('1')
    G.add_vertex('2')
    G.add_vertex('3')
    G.add_vertex('4')
    G.add_vertex('5')
    G.add_edge(0, 2)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(5, 3)
    G.add_edge(3, 4)
    G.add_edge(1, 0)
    print(G.size())
    print(G)
    print(G.visualize())

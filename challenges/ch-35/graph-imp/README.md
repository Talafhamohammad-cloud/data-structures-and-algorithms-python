# Graphs
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges
## Challenge
**Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:**

***add node***
Arguments: value
Returns: The added node
Add a node to the graph
***add vertix***
Arguments: 2 nodes to be connected by the edge, weight (optional)
Returns: nothing
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
***get vertices***
Arguments: none
Returns all of the nodes in the graph as a collection (set, list, or similar)
***get neighbors***
Arguments: node
Returns a collection of edges connected to the given node
Include the weight of the connection in the returned collection
***size***
Arguments: none
Returns the total number of nodes in the graph
## Approach & Efficiency
add_vertix:
    Time O(1)
    Space O(1)
add_edge:
    Time O(n)
    Space O(n)
get_vertices:
    Time O(n)
    Space O(n)
get_neighbors:
    Time O(n)
    Space O(n)
size:
    Time O(1)
    Space O(1)
## API
### dd vertix: Add a vertix to the graph, Arguments: value , Returns: The added vertix
### add edge: Adds a new edge between two nodes in the graph If specified, assign a weight to the edge Both nodes should already be in the Graph ,Arguments: 2 nodes to be connected by the edge, weight (optional) , Returns: nothing
### get vertices: Returns all of the vertices in the graph as a collection (set, list, or similar)
### get neighbors: Returns a collection of edges connected to the given node , Include the weight of the connection in the returned collection
### size: Returns the total number of nodes in the graph

## PR LINK:
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/50 

########################################################################
########### code challenge-36 (graph-breadth-first)####################
#######################################################################

# Challenge Summary
Extending an Implementation to Implement a breadth-first traversal on a graph.
Write the following method for the Graph class:
breadth first
Arguments: vertex
Return: A collection of vertices in the order they were visited.
Display the collection
## Whiteboard Process:
![imgs](img/whiteBoerd.jpg)

## Approach & Efficiency:
Time: O(n^2)
Space: O(n)
## Solution:
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

## NOTE: the challenge is solved with strech goals to find if there is path between two vertices or not         
## PR LINK :
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/51

#######################################################################
########### code challenge-37 (graph-business-trip)####################
#######################################################################
# Challenge Summary
Write a function called business trip
Arguments: graph, array of city names
Return: cost or null
## Whiteboard Process
![image](img/trip.jpg)
## Approach & Efficiency
Time = O(n^2)
Space = O(n)
## Solution
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

## PR LINK:
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/52

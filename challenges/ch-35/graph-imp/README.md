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
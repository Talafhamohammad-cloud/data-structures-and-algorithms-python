# Singly Linked List

A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail).
Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.
The first node is called the head; it points to the first node of the list and helps us access every other element in the list. The last node, also sometimes called the tail, points to NULL which helps us in determining when the list ends.

## Challenge:

Creat two classes:

### 1-Node

Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

### 2-Linked List

Create a Linked List class
Within your Linked List class, include a head property.
Upon instantiation, an empty Linked List should be created.
The class should contain the following methods
insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.
content
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.
**str**
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

## Approach & Efficiency

Node class that has properties for the value stored in the Node, and a pointer to the next Node, LinkedList class, include a head property. Upon instantiation, an empty Linked.
and about the efficiency
| name         |space | time |
|##############|######|######|
|insert        | O(1) | O(1) |
|append        | O(n) | O(n) |
|string        | O(n) | O(n) |
|includes      | O(n) | O(n) |
|insert-after  | O(1) | O(n) |
|insert-before | O(1) | O(n) |
## API:

### insert

Takes any value as an argument and adds a new node with that value to the head of the list.

### append

Takes any value as an argument and adds a new node with that value to the end of the list.

### content

Takes any value as an argument and returns (T) if its exist and (F) if not

### "_str__"
its without arguments and returns a string represent all the values in the Linked List

## insert before
this method takes two arguments the first one is the node wher i want to add before and 
the second one the new value that i want to add 

## isert after 
it works the same as insert before but here we will add after specific node and its also contains two arguments 
the node i want to add  after and the new value 


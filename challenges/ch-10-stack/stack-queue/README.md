# Stacks and Queues implemintation :
### Stack:
A stack is a data structure which implements a LIFO policy, i.e. the element deleted from the stack is the one most recently inserted The INSERT operation on a stack is often called Push, and the DELETE operation, is often called Pop We can implement a stack of at most n elements with an array S[1…n], where top[S] is the most recently inserted element, the stack cosists of elements S[1…top[S]], wehre V[1] is the elemt at the bottom and, S[top[S]] is the element at the top. If top[V]=0 then the stack is empty.

### queue:
The queue is a data structure which implements the FIFO policy, i.e. the deleted element is the one which is in the queue for the longest time We call the INSERT operation on a queue ENQUEUE, and the DELETE operation DEQUEUE. The index of the first element is head[Q], the index of the next inserted element is tail[Q]. The elements in the queue are in the locations head[Q], head[Q]+1,…, tail[Q]-1, and the queue is empty if head[Q]=tail[Q]. Initially we have head[Q]=tail[Q]=1. If head[Q]=tail[Q]+1 then the queue is full.
## challenge:
Create stack and queue classes and add to stack push, pop, peek and is empty methods. and for queue enqueue, dequeue, peek and is empty methods

## Approach & Efficiency:
***Stacks***
1-push >>> O(1)
2-pop >>> O(1)
3-peek >>> O(1)
4-is_empty >>> O(1)
***Queues***
1-enqueue >>> O(1)
2-dequeue >>> O(1)
3-peek >>> O(1)
4-is_empty >>> O(1)

## API
### Stacks:
-pushto push onto a stack and push multiple values onto a stack
-pop to pop off the stack or empty a stack after multiple pops
-peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
-is_empty returns true when stack is empty otherwise returns false.

### Queues:
-enqueue Nodes or items that are added to the queue.
-dequeue Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
-peek When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
-is_empty returns true when queue is empty otherwise returns false.
## PR link:
https://github.com/Talafhamohammad-cloud/data-structures-and-algorithms-python/pull/19 
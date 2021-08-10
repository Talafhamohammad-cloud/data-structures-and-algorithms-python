from stack_queue import __version__
from stack_queue.stack_queue import (Stack,Queue)

def test_version():
    assert __version__ == '0.1.0'
############################################-these tests orderd according to the requierment of the challenges-#####################
##################################(1)##########################################
def test_push():
    stack = Stack()
    stack.push(1)
    excepted = stack.top.value
    assert excepted == 1
##################################(2)##########################################
def test_push2():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    excepted = stack.top.value
    assert excepted == 2
##################################(3)##########################################
def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    actual = stack.pop()
    expected = 2
    assert actual == expected
##################################(4)##########################################
def test_pop2():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    actual = stack.top
    expected = None
    assert actual == expected
##################################(5)##########################################
def test_peek():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    expected = 4
    actual = stack.peek()
    assert actual == expected
##################################(6)##########################################
def test_init_empty():
   stack = Stack()
   expected = None
   assert expected == stack.top
##################################(7)##########################################
def test_raise_stack():
   stack = Stack()
   expected = "empty stack"
   assert expected == stack.peek()
##################################(8)##########################################
def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.front.value
    expected = 1
    assert expected == actual
##################################(9)##########################################
def test_enqueue2():
    queue = Queue()
    queue.enqueue('mohammad')
    queue.enqueue('khaled')
    actual = queue.front.next.value
    expected = 'khaled'
    assert expected == actual
##################################(10)##########################################
def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    actual = queue.front.value
    expected = 2
    assert expected == actual
##################################(11)##########################################
def test_peek_dedueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    expected = 1
    actual = queue.peek()
    assert actual == expected
##################################(12)##########################################
def test_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual == expected
##################################(13)##########################################
def test_init_empty_queue():
  queue = Queue()
  expected = None
  assert expected == queue.front
##################################(14)##########################################
def test_raise_queue():
   queue = Queue()
   expected = "Empty queue"
   assert expected == queue.peek()

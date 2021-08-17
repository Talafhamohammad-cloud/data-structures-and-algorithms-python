from stack_queue_pseudo import __version__
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue

def test_version():
    assert __version__ == '0.1.0'
################################################################
def test_input_multi():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(1)
    Pseudoqueue.enqueue(2)
    Pseudoqueue.enqueue(3)
    actual = Pseudoqueue.rear
    expected = 3
    assert expected == actual
##################################################################
def test_pseudo():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(0)
    Pseudoqueue.enqueue(1)
    Pseudoqueue.enqueue(2)
    Pseudoqueue.dequeue()
    Pseudoqueue.dequeue()
    actual = Pseudoqueue.dequeue()
    expected = 2
    assert expected == actual
#################################################################
def test_empty():
    Pseudoqueue = PseudoQueue()
    actual = Pseudoqueue.dequeue()
    expected = None
    assert expected == actual

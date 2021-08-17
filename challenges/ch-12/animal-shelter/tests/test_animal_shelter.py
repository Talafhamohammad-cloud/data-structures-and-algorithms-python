from animal_shelter import __version__
from animal_shelter.animal_shelter import (AnimalShelter,Node,Queue)

def test_version():
    assert __version__ == '0.1.0'
##########################################################
def test_enqueue():
    actual = []
    animal = AnimalShelter()
    animal.enqueue('rex', 'dog')
    actual += [animal.dog.peek()]
    animal.enqueue('flora', 'cat')
    actual += [animal.cat.peek()]
    excepted = ['rex', 'flora']
    assert actual == excepted
#########################################################################
def test_enqueue_fail():
    animal = AnimalShelter()
    actual = animal.enqueue('pummy', 'hamster')
    excepted = 'you have to choose cat or dog'
    assert actual == excepted
###########################################################################
def test_dequeue():
    animal = AnimalShelter()
    animal.enqueue('max', 'dog')
    animal.enqueue('kresti', 'cat')
    actual = [animal.dequeue('dog'), animal.dequeue('cat')]
    excepted = ['max', 'kresti']
    assert actual == excepted
#############################################################################
def test_dequeue_fail():
    animal = AnimalShelter()
    actual = animal.dequeue('rabbit')
    excepted = 'you have to choose cat or dog'
    assert actual == excepted

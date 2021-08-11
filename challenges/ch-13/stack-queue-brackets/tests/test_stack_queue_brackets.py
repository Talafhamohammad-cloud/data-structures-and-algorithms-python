from stack_queue_brackets import __version__
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_version():
    assert __version__ == '0.1.0'
#########################################################
def test_one():
    string = "{[]{(hello)}}"
    actual=validate_brackets(string)
    expected="valid"
    assert actual==expected
######################################################### 
def test_two():
    string = "{]()}}"
    actual = validate_brackets(string)
    expected = "invalid"
    assert actual == expected
############################################################
def test_three():
    string = "{[]{}}"
    actual = validate_brackets(string)
    expected = "valid"
    assert actual == expected
############################################################
def test_four():
    string = "[]()}"
    actual = validate_brackets(string)
    expected = "invalid"
    assert actual == expected

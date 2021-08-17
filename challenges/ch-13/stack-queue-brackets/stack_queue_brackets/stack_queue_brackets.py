open_brackets = ["[","{","("]
close_brackets = ["]","}",")"]
def validate_brackets(string):
    stack = []
    for i in string:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if ((len(stack) > 0) and
                (open_brackets[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "invalid"
    if len(stack) == 0:
        return "valid"
    else:
        return "invalid"




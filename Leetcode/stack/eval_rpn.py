import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def eval_rpn(tokens):
    import operator
    stack = []
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': lambda x, y: int(x / y)
    }

    for token in tokens:
        if token in ops:
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[token](b, a))
        else:
            stack.append(int(token))

    return stack[0]

test_cases = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
]

run_tests(eval_rpn, test_cases)
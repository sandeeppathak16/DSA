import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def removeOuterParentheses(s):
    depth = 0
    result = []

    for ch in s:
        if ch == '(':
            if depth > 0:
                result.append(ch)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(ch)
    
    return "".join(result)
    


test_cases = [
    # LeetCode examples
    (("(()())(())",), "()()()"),
    (("(()())(())(()(()))",), "()()()()(())"),
    (("()()",), ""),

    # Single primitive
    (("(())",), "()"),
    (("((()))",), "(())"),
    (("()",), ""),

    # Multiple primitives
    (("(())(())",), "()()"),
    (("((()))(()())",), "(())()()"),

    # Nested
    (("(((())))",), "((()))"),
    (("(()(()))",), "()(())"),

    # Small cases
    (("((()))()",), "(())"),
    (("()(())",), "()"),

    # Deep nesting
    (("(((((())))))",), "((((()))))"),
]

run_tests(removeOuterParentheses, test_cases)
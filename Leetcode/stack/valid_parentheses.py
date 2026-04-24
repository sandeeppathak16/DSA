import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def is_valid(string):
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []

    for s in string:
        if s in mapping:
            if not stack or stack.pop() != mapping[s]:
                return False

        else:
            stack.append(s)

    
    return len(stack) == 0

test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("([)]", False),
]

run_tests(is_valid, test_cases)
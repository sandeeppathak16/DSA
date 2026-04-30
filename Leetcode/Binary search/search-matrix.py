import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])

    l, r = 0, rows * cols - 1

    while l <= r:
        m = (l + r) // 2

        val = matrix[m // cols][m % cols]

        if val == target:
            return True

        elif val < target:
            l = m + 1

        else:
            r = m - 1

    return False
    

test_cases = [
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3,), True),
    (([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13,), False),
]

run_tests(search_matrix, test_cases)
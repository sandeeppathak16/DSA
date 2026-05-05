import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def set_zero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_cols.add(c)
                zero_rows.add(r)


    for r in zero_rows:
        for c in range(cols):
            matrix[r][c] = 0

    
    for c in zero_cols:
        for r in range(rows):
            matrix[r][c] = 0

    return matrix



test_cases = [
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
]

run_tests(set_zero, test_cases)
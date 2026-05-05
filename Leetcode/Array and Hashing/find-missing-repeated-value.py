
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def find_missing_repeated_value(grid):
    rows = len(grid)
    cols = len(grid[0])

    n = rows * cols
    repeated = -1

    for i in range(n):
        val = abs(grid[i // cols][i % cols])

        r = (val - 1) // cols
        c = (val - 1) % cols

        if grid[r][c] > 0:
            grid[r][c] = -grid[r][c]

        else:
            repeated = val

    missing = -1

    for i in range(n):
        if grid[i // cols][i % cols] > 0:
            missing = i + 1
            break

    return [repeated, missing]

test_cases = [
    ([[1,3],[2,2]], [2,4]),
    ([[9,1,7],[8,9,2],[3,4,6]], [9,5]),
]

run_tests(find_missing_repeated_value, test_cases)
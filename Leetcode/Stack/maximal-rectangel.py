import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def maximalRectangle(matrix):
    if not matrix:
        return 0
    
    cols = len(matrix[0])
    heights = [0] * (cols + 1)
    ans = 0

    for row in matrix:
        for c in range(cols):
            if row[c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0

        stack = [-1]

        for i in range(cols + 1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)

            stack.append(i)

    return ans



test_cases = [
    # Empty matrix
    ([], 0),

    # Single cell
    ([["0"]], 0),
    ([["1"]], 1),

    # Single row
    ([["1", "1", "1", "1"]], 4),
    ([["1", "0", "1", "1"]], 2),

    # Single column
    ([["1"], ["1"], ["1"]], 3),
    ([["1"], ["0"], ["1"]], 1),

    # All zeros
    ([
        ["0", "0"],
        ["0", "0"],
    ], 0),

    # All ones
    ([
        ["1", "1"],
        ["1", "1"],
    ], 4),

    # LeetCode Example
    ([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ], 6),

    # Entire matrix is rectangle
    ([
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"],
    ], 9),

    # Largest rectangle in middle
    ([
        ["0", "1", "1", "0"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "0"],
    ], 8),

    # Checkerboard
    ([
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ], 1),

    # Horizontal rectangle
    ([
        ["0", "0", "0", "0"],
        ["1", "1", "1", "1"],
        ["0", "0", "0", "0"],
    ], 4),

    # Vertical rectangle
    ([
        ["0", "1", "0"],
        ["0", "1", "0"],
        ["0", "1", "0"],
        ["0", "1", "0"],
    ], 4),

    # Complex case
    ([
        ["1", "1", "0", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "1"],
    ], 6),

    # Another complex case
    ([
        ["1", "0", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "0"],
    ], 6),
]

run_tests(maximalRectangle, test_cases)

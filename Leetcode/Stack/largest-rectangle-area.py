import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def largestRectangleArea(heights):
    max_area = float("-inf")

    n = len(heights)
    stack = []

    for i, h in enumerate(heights):
        curr = i
        while stack and h < stack[-1][1]:
            max_area = max(max_area, ((i - stack[-1][0]) * stack[-1][1]))
            curr = stack[-1][0]
            stack.pop()

        stack.append([curr, h])

    for i, h in stack:
        max_area = max(max_area, ((n - i) * h))

    return max_area



test_cases = [
    # LeetCode examples
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),

    # Single bar
    ([1], 1),

    # Two bars
    ([1, 2], 2),
    ([2, 1], 2),

    # Increasing heights
    ([1, 2, 3, 4, 5], 9),

    # Decreasing heights
    ([5, 4, 3, 2, 1], 9),

    # All equal
    ([3, 3, 3, 3], 12),

    # Contains zero
    ([2, 0, 2], 2),

    # All zeros
    ([0, 0, 0], 0),

    # Plateau
    ([2, 2, 2], 6),

    # Valley
    ([2, 1, 2], 3),

    # Mixed heights
    ([4, 2, 0, 3, 2, 5], 6),

    # Another common example
    ([6, 7, 5, 2, 4, 5, 9, 3], 16),
]

run_tests(largestRectangleArea, test_cases)

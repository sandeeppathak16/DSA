import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def longest_ractangle(heights):
    maxArea = float('-inf')
    stack = []

    for i, h in enumerate(heights):
        curr = i

        while stack and h < stack[-1][1]:
            maxArea = max(maxArea, ((i - stack[-1][0]) * stack[-1][1]))
            curr = stack[-1][0]
            stack.pop()

        stack.append([curr, h])

    for i, h in stack:
        maxArea = max(maxArea, (len(heights) - i) * h)

    return maxArea

test_cases = [
    ([2,1,5,6,2,3], 10),
    ([2,4], 4),
]

run_tests(longest_ractangle, test_cases)
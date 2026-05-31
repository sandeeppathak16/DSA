import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def next_greater_2(nums):
    stack = []
    n = len(nums)

    ans = [0] * n

    for i in range(2*n - 1, -1, -1):
        current = nums[i % n]

        while stack and stack[-1] <= current:
            stack.pop()

        if i < n:
            ans[i] = stack[-1] if stack else -1

        stack.append(current)

    return ans

test_cases = [
    ([1, 2, 1], [2, -1, 2]),

    ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),

    ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),

    ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),

    ([2, 2, 2], [-1, -1, -1]),

    ([3, 1, 2], [-1, 2, 3]),

    ([1], [-1]),

    ([2, 1], [-1, 2]),

    ([1, 5, 3, 6, 8], [5, 6, 6, 8, -1]),

    ([8, 1, 2, 3, 4], [-1, 2, 3, 4, 8]),
]

run_tests(next_greater_2, test_cases)
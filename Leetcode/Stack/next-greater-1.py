import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def next_greater_1(nums1, nums2):
    stack = []
    n = len(nums2)

    from collections import defaultdict

    next_greater = defaultdict(int)

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()

        next_greater[nums2[i]] = stack[-1] if stack else -1

        stack.append(nums2[i])

    ans = []

    for ele in nums1:
        ans.append(next_greater[ele])

    return ans

test_cases = [
    (
        ([4, 1, 2], [1, 3, 4, 2]),
        [-1, 3, -1]
    ),
    (
        ([2, 4], [1, 2, 3, 4]),
        [3, -1]
    ),
    (
        ([1, 3], [1, 2, 3, 4]),
        [2, 4]
    ),
    (
        ([1], [1]),
        [-1]
    ),
    (
        ([3, 1], [1, 3, 4, 2]),
        [4, 3]
    ),
]

run_tests(next_greater_1, test_cases)
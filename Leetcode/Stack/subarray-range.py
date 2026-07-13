import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests

import operator


def get_indices(arr, reverse, should_pop, default):
    n = len(arr)
    result = [default] * n
    stack = []

    indices = range(n - 1, -1, -1) if reverse else range(n)

    for i in indices:
        while stack and should_pop(arr[stack[-1]], arr[i]):
            stack.pop()

        result[i] = stack[-1] if stack else default

        stack.append(i)

    return result


def subArrayRanges(nums):
    n = len(nums)

    pre_smaller = get_indices(
        nums,
        reverse=False,
        should_pop=operator.ge,
        default=-1
    )

    next_smaller = get_indices(
        nums,
        reverse=True,
        should_pop=operator.gt,
        default=n
    )

    pre_greater = get_indices(
        nums,
        reverse=False,
        should_pop=operator.le,
        default=-1
    )

    next_greater = get_indices(
        nums,
        reverse=True,
        should_pop=operator.lt,
        default=n
    )

    ans = 0

    for i, value in enumerate(nums):
        max_count = (i - pre_greater[i]) * (next_greater[i] - i)
        min_count = (i - pre_smaller[i]) * (next_smaller[i] - i)

        ans += value * (max_count - min_count)
    
    return ans


test_cases = [
    (
        ([1, 2, 3],),
        4
    ),
    (
        ([1, 3, 3],),
        4
    ),
    (
        ([4, -2, -3, 4, 1],),
        59
    ),
    (
        ([1],),
        0
    ),
    (
        ([2, 2],),
        0
    ),
    (
        ([2, 2, 2],),
        0
    ),
    (
        ([3, 1, 2, 4],),
        13
    ),
    (
        ([1, 2],),
        1
    ),
    (
        ([2, 1],),
        1
    ),
    (
        ([1, 2, 1],),
        3
    ),
    (
        ([5, 4, 3, 2, 1],),
        20
    ),
    (
        ([1, 2, 3, 4, 5],),
        20
    ),
]

run_tests(subArrayRanges, test_cases)
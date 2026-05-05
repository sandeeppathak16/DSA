import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def search_insert(nums, target):
    l = 0
    r = len(nums) - 1

    ans = len(nums)

    while l <= r:
        m = (l + r) // 2

        if nums[m] >= target:
            ans = m
            r = m - 1
        else:
            l = m + 1

    return ans
    
            


test_cases = [
    # basic cases
    (([1, 2, 5, 7, 10], 5), 2),     # exact match
    (([1, 2, 5, 7, 10], 6), 3),     # insert in middle
    (([1, 2, 5, 7, 10], 0), 0),     # smaller than all
    (([1, 2, 5, 7, 10], 11), 5),    # greater than all

    # duplicates
    (([1, 2, 2, 2, 5], 2), 1),      # first occurrence
    (([2, 2, 2, 2], 2), 0),         # all same
    (([2, 2, 2, 2], 3), 4),         # insert after duplicates

    # single element
    (([5], 5), 0),                  # match
    (([5], 3), 0),                  # insert before
    (([5], 7), 1),                  # insert after

    # empty array
    (([], 10), 0),

    # negative numbers
    (([-10, -5, 0, 3, 8], -5), 1),
    (([-10, -5, 0, 3, 8], -6), 1),

    # edge positions
    (([1, 3, 5, 7], 2), 1),
    (([1, 3, 5, 7], 4), 2),
    (([1, 3, 5, 7], 6), 3),

    # large gap jumps
    (([1, 100, 200, 300], 150), 2),

    # already sorted but large duplicates at ends
    (([1, 1, 1, 1, 5, 6, 7], 1), 0),
    (([1, 2, 3, 9, 9, 9], 9), 3),
]

run_tests(search_insert, test_cases)
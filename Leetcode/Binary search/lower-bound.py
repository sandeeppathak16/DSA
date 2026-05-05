import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def lower_bound(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        m = (l + r) // 2

        if nums[m] < target:
            l = m + 1
        else:
            r = m

    return l 
            


test_cases = [
    (([1, 2, 5, 7, 10], 5), 2),     # exact match
    (([1, 2, 5, 7, 10], 6), 3),     # first ≥ 6 is 7
    (([1, 2, 5, 7, 10], 0), 0),     # smaller than all
    (([1, 2, 5, 7, 10], 11), 5),    # greater than all (n)
    (([1, 2, 2, 2, 5], 2), 1),      # duplicates → first occurrence
    (([-10, -5, 0, 3, 8], -5), 1),  # negative numbers
]

run_tests(lower_bound, test_cases)
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def upper_bound(nums, target):
    l = 0
    r = len(nums) - 1
    ans = len(nums)

    while l <= r:
        m = (l + r) // 2

        if nums[m] > target:
            ans = m
            r = m - 1
        else:
            l = m + 1

    return ans 

    
            


test_cases = [
    (([1, 2, 5, 7, 10], 5), 3),     # first > 5 is 7
    (([1, 2, 5, 7, 10], 6), 3),     # first > 6 is 7
    (([1, 2, 5, 7, 10], 10), 5),    # no element > 10
    (([1, 2, 5, 7, 10], 0), 0),     # first > 0 is 1
]

test_cases += [
    (([1, 2, 2, 2, 5], 2), 4),      # skip all 2s → index of 5
    (([1, 1, 1, 1], 1), 4),         # all equal → return n
]

test_cases += [
    (([-10, -5, 0, 3, 8], -5), 2),  # first > -5 is 0
    (([-10, -5, 0, 3, 8], -11), 0), # first > -11 is -10
]

test_cases += [
    (([], 5), 0),                   # empty array
    (([5], 5), 1),                  # single element equal
    (([5], 3), 0),                  # single element greater
    (([5], 10), 1),                 # single element smaller
]

run_tests(upper_bound, test_cases)
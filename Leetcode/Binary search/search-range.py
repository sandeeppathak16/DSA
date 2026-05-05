import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def search_range(nums, target):
    def binary_search(first_index):
        l = 0
        r = len(nums) - 1

        index = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                index = m
                if first_index:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return index
    
    return [binary_search(True), binary_search(False)]
    
            


test_cases = [
    # basic cases
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 7), [1, 2]),
    (([5, 7, 7, 8, 8, 10], 5), [0, 0]),
    (([5, 7, 7, 8, 8, 10], 10), [5, 5]),

    # not found
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    (([], 1), [-1, -1]),

    # single element
    (([1], 1), [0, 0]),
    (([1], 0), [-1, -1]),

    # all elements same
    (([2, 2, 2, 2, 2], 2), [0, 4]),
    (([2, 2, 2, 2, 2], 3), [-1, -1]),

    # duplicates at edges
    (([1, 2, 2, 2, 3], 2), [1, 3]),
    (([2, 2, 2, 3, 4], 2), [0, 2]),
    (([1, 2, 3, 4, 4, 4], 4), [3, 5]),

    # negative numbers
    (([-5, -3, -3, -3, 0, 2], -3), [1, 3]),
    (([-5, -3, -3, -3, 0, 2], -4), [-1, -1]),

    # target at boundaries
    (([1, 3, 5, 7, 9], 1), [0, 0]),
    (([1, 3, 5, 7, 9], 9), [4, 4]),

    # large duplicate block in middle
    (([1, 2, 3, 4, 4, 4, 4, 5, 6], 4), [3, 6]),

    # two elements
    (([2, 2], 2), [0, 1]),
    (([2, 3], 2), [0, 0]),
    (([2, 3], 3), [1, 1]),
]

run_tests(search_range, test_cases)
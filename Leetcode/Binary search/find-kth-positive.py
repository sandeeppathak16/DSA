import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def find_kth_positive(arr, k):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        missing = arr[m] - (m + 1)

        if missing < k:
            l = m + 1
        else:
            r = m - 1

    return k + r + 1


test_cases = [
    # Basic examples
    (([2,3,4,7,11], 5), 9),
    (([1,2,3,4], 2), 6),

    # Missing starts from 1
    (([2], 1), 1),
    (([2], 2), 3),

    # No missing until after array
    (([1,2,3,4,5], 1), 6),
    (([1,2,3,4,5], 5), 10),

    # Single element arrays
    (([1], 1), 2),
    (([5], 1), 1),
    (([5], 4), 4),
    (([5], 5), 6),

    # Consecutive array
    (([1,2,3,4,5,6,7,8], 3), 11),

    # Large gaps
    (([10,20,30], 1), 1),
    (([10,20,30], 9), 9),
    (([10,20,30], 10), 11),

    # Missing inside array
    (([1,3,5,7,9], 4), 8),

    # Array with large numbers
    (([100], 99), 99),
    (([100], 100), 101),

    # Edge cases
    (([1], 100), 101),
    (([2,4,6,8], 5), 9),

    # Continuous missing pattern
    (([1,3,4,8], 5), 9),

    # Bigger test
    (([2,5,9,15,20], 10), 13),
]

run_tests(find_kth_positive, test_cases)
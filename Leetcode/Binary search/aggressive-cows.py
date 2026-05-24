import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def aggressive_cows(stalls, k):
    


test_cases = [
    # Basic examples
    (([1, 2, 4, 8, 9], 3), 3),
    (([10, 1, 2, 7, 5], 3), 4),
    (([2, 12, 11, 3, 26, 7], 5), 1),

    # Minimum input
    (([1, 2], 2), 1),

    # Large gaps
    (([1, 10, 20, 30, 40], 2), 39),

    # All cows in consecutive stalls
    (([1, 2, 3, 4, 5], 5), 1),

    # Only two cows
    (([1, 2, 8, 12, 17], 2), 16),

    # Sorted uneven gaps
    (([1, 3, 7, 9, 13], 3), 6),

    # Unsorted input
    (([9, 1, 8, 2, 4], 3), 3),

    # Large answer
    (([1, 100, 200, 300, 400], 3), 199),

    # Cows almost equal to stalls
    (([1, 2, 4, 8, 16], 4), 2),

    # Tight placement
    (([1, 2, 3, 100], 3), 2),

    # Prime-number positions
    (([2, 3, 5, 7, 11, 13], 3), 5),

    # Bigger array
    (([1, 5, 9, 13, 17, 21, 25], 4), 8),

    # Very sparse stalls
    (([1, 1000, 2000, 3000, 4000], 5), 999),

    # k = 1
    (([1, 2, 3, 4, 5], 1), 0),

    # Two stalls very far apart
    (([1, 1000000000], 2), 999999999),

    # Medium random case
    (([4, 8, 15, 16, 23, 42], 3), 19),

    # Alternate spacing
    (([1, 4, 7, 10, 13, 16], 3), 6),

    # Dense cluster + far stall
    (([1, 2, 3, 4, 100], 2), 99),

    # Edge case where optimal split is tricky
    (([1, 2, 4, 6, 8, 9], 3), 3),
]

run_tests(aggressive_cows, test_cases)
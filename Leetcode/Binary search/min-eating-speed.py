import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def min_eating_speed(piles, h):
    l, r = 1, max(piles)

    while l <= r:
        m = (l + r) // 2

        val = 0

        for pile in piles:
            val += (pile + m - 1) // m

        if val <= h:
            r = m - 1

        else:
            l = m + 1

    return l
    

test_cases = [
    (([3,6,7,11], 8,), 4),
    (([30,11,23,4,20], 5,), 30),
    (([30,11,23,4,20], 6,), 23),
]

run_tests(min_eating_speed, test_cases)

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def max_product(nums):
    res = float('-inf')
    maxres, minres = 1, 1

    for num in nums:
        temp = maxres * num
        maxres = max(num, temp, minres*num)

        minres = min(num, temp, minres*num)
        res = max(res, maxres)

    return res



test_cases = [
    # Basic cases
    ([2,3,-2,4], 6),         
    ([-2,0,-1], 0),

    # Single element
    ([5], 5),
    ([-5], -5),

    # All negatives (even count)
    ([-1,-2,-3,-4], 24),

    # All negatives (odd count)
    ([-1,-2,-3], 6),

    # Includes zero splitting segments
    ([0,2], 2),
    ([-2,0,-1,4], 4),

    # Large positive product
    ([1,2,3,4], 24),

    # Mixed case
    ([2,-5,-2,-4,3], 24),

    # Leading negative
    ([-2,3,-4], 24),

    # Multiple zeros
    ([0,0,0], 0),

    # Edge tricky case
    ([-2,3,-4,-1], 24),
]
run_tests(max_product, test_cases)
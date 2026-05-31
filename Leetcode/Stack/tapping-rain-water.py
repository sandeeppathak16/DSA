import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def trap(height):
    i = 0
    j = len(height) - 1
    res = 0

    lmax, rmax = height[i], height[j]

    while i < j:
        if lmax < rmax:
            i += 1
            lmax = max(lmax, height[i])
            res += (lmax - height[i])
        else:
            j -= 1
            rmax = max(rmax, height[j])
            res += (rmax - height[j])

    return res
    



test_cases = [
    # LeetCode example
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),

    # LeetCode example 2
    ([4,2,0,3,2,5], 9),

    # Single bar
    ([1], 0),

    # Two bars
    ([1,2], 0),

    # Increasing heights
    ([1,2,3,4,5], 0),

    # Decreasing heights
    ([5,4,3,2,1], 0),

    # Simple bowl
    ([2,0,2], 2),

    # Wider bowl
    ([3,0,0,3], 6),

    # Multiple pits
    ([3,0,2,0,4], 7),

    # Deep pit
    ([5,0,0,0,5], 15),

    # Equal heights
    ([3,3,3,3], 0),

    # Small valley
    ([1,0,1], 1),

    # Valley with unequal walls
    ([4,1,3], 2),

    # Large wall at end
    ([5,4,1,2], 1),

    # Complex case
    ([0,3,0,1,0,2,0,4], 12),
]

run_tests(trap, test_cases)
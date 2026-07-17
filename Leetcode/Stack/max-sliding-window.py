import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def maxSlidingWindow(nums, k):
    from collections import deque

    dq = deque()

    n = len(nums)

    ans = []

    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        
        dq.append(i)

        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans



test_cases = [
    # LeetCode example
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),

    # Single element
    (([5], 1), [5]),

    # Window size is 1
    (([4, 2, 7, 1], 1), [4, 2, 7, 1]),

    # Window size equals array size
    (([2, 1, 3], 3), [3]),

    # Increasing sequence
    (([1, 2, 3, 4, 5], 2), [2, 3, 4, 5]),

    # Decreasing sequence
    (([5, 4, 3, 2, 1], 2), [5, 4, 3, 2]),

    # All elements equal
    (([2, 2, 2, 2], 2), [2, 2, 2]),

    # Negative numbers
    (([-4, -2, -5, -1], 2), [-2, -2, -1]),

    # Duplicate maximums
    (([1, 3, 3, 2, 5], 3), [3, 3, 5]),

    # Duplicate maximum leaving the window
    (([4, 4, 1, 2], 2), [4, 4, 2]),

    # Maximum at beginning
    (([9, 1, 2, 3], 2), [9, 2, 3]),

    # Maximum at end
    (([1, 2, 3, 9], 2), [2, 3, 9]),

    # Large window
    (([8, 5, 10, 7, 9, 4, 15, 12], 4), [10, 10, 10, 15, 15]),

    # Alternating highs and lows
    (([1, 100, 1, 100, 1], 2), [100, 100, 100, 100]),

    # k = n
    (([7, 2, 4], 3), [7]),

    # Two elements
    (([1, 2], 2), [2]),
    (([2, 1], 2), [2]),

    # Duplicate values
    (([1, 1, 1, 1], 3), [1, 1]),

    # Mixed duplicates
    (([4, 2, 2, 2, 5], 3), [4, 2, 5]),

    # Negative and positive
    (([-1, 5, 3, -2, 6], 2), [5, 5, 3, 6]),

    # k = n = 1
    (([10], 1), [10]),
]

run_tests(maxSlidingWindow, test_cases)

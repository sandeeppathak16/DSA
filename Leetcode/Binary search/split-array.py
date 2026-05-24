import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def split_array(nums, k):
    l = max(nums)
    r = sum(nums)

    while l <= r:
        m = (l + r) // 2

        s = 1
        cnt = 0

        for num in nums:
            if cnt + num <= m:
                cnt += num
            else:
                s += 1
                cnt = num

        if s > k:
            l = m + 1
        else:
            r = m - 1

    return l
    


test_cases = [
    # Basic examples
    (([7,2,5,10,8], 2), 18),
    (([1,2,3,4,5], 2), 9),
    (([1,4,4], 3), 4),

    # Single element
    (([10], 1), 10),

    # Split each element individually
    (([1,2,3,4], 4), 4),

    # Only one partition
    (([1,2,3,4], 1), 10),

    # Equal numbers
    (([5,5,5,5], 2), 10),
    (([5,5,5,5], 3), 10),

    # Increasing sequence
    (([1,2,3,4,5,6,7,8,9], 3), 17),

    # Decreasing sequence
    (([9,8,7,6,5], 2), 18),

    # Large value in middle
    (([1,1,1,100,1,1], 2), 102),

    # Exact partition possible
    (([2,2,2,2,2,2], 3), 4),

    # Large numbers
    (([1000000,1000000,1000000], 2), 2000000),

    # More partitions than needed
    (([1,2,3], 3), 3),

    # Tricky balancing
    (([10,20,30,40], 2), 60),

    # Another balancing case
    (([1,10,10,1], 2), 11),

    # Heavy last element
    (([1,1,1,50], 2), 50),

    # Alternating values
    (([1,100,1,100,1], 3), 101),

    # Large partition count
    (([7,7,7,7,7,7], 6), 7),

    # Tight split
    (([3,1,4,1,5,9,2], 3), 11),
]

run_tests(split_array, test_cases)
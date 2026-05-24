import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def ship_with_in_days(weights, days):
    l = max(weights)
    r = sum(weights)

    while l <= r:
        m = (l + r) // 2

        days_needed = 1
        current_sum = 0

        for w in weights:
            if current_sum + w > m:
                days_needed += 1
                current_sum = w
            else:
                current_sum += w

        if days_needed <= days:
            r = m - 1
        else:
            l = m + 1

    return l
    


test_cases = [
    # Basic examples
    (([1,2,3,4,5,6,7,8,9,10], 5), 15),
    (([3,2,2,4,1,4], 3), 6),
    (([1,2,3,1,1], 4), 3),

    # Single package
    (([10], 1), 10),

    # Days equal to number of packages
    (([5,4,3,2,1], 5), 5),

    # One single day -> must carry all
    (([5,4,3,2,1], 1), 15),

    # Large weight in middle
    (([1,1,1,100,1,1], 3), 100),

    # All same weights
    (([5,5,5,5,5], 5), 5),
    (([5,5,5,5,5], 2), 15),

    # Increasing sequence
    (([1,2,3,4,5], 2), 9),

    # Decreasing sequence
    (([9,8,7,6,5], 3), 15),

    # Capacity must be max element
    (([10,50,100,100,50,10], 5), 100),

    # Tight partition
    (([7,2,5,10,8], 2), 18),

    # Very large numbers
    (([1000000,1000000,1000000], 2), 2000000),

    # Edge case with many days
    (([1,2,3], 10), 3),

    # Minimal split
    (([1,2,3,4,5], 3), 6),

    # Another tricky case
    (([10,10,10,10], 3), 20),

    # Heavy last package
    (([1,1,1,1,50], 2), 50),

    # Alternating weights
    (([1,100,1,100,1], 3), 101),

    # Exact fit partitions
    (([2,2,2,2,2,2], 3), 4),

    # Large days but not enough for 1 capacity
    (([9,9,9,9], 4), 9),
]

run_tests(ship_with_in_days, test_cases)

run_tests(ship_with_in_days, test_cases)
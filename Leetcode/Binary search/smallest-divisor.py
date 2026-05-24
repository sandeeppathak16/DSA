import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def smallest_divisor(nums, threshold):
    l = 1
    r = max(nums)
    
    while l <= r:
        m = (l + r) // 2

        val = 0

        for num in nums:
            val += (num + m - 1) // m

        if val <= threshold:
            r = m - 1
        else:
            l = m + 1

    return l

test_cases = [
    (([1, 2, 5, 9], 6), 5),
    (([44, 22, 33, 11, 1], 5), 44),
    (([21212, 10101, 12121], 1000000), 1),
    (([2, 3, 5, 7, 11], 11), 3),
    (([19], 5), 4),
    (([1, 1, 1, 1], 4), 1),
    (([1000000], 1), 1000000),
    (([8, 4, 2, 3], 10), 2),
    (([5, 9, 13, 17], 8), 9),
    (([10, 20, 30], 7), 10),
]

run_tests(smallest_divisor, test_cases)
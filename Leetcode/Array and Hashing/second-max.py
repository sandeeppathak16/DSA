import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def second_max(nums):
    if len(nums) < 2:
        return None

    first, second = None, None

    for num in nums:
        if first is None or num > first:
            if num != first:
                second = first

            first = num

        elif num != first and (second is None or num > second):
            second = num

    return second
    

test_cases = [
    ([8, 8, 7, 6, 5], 7),
    ([10, 10, 10, 10, 10], None),
    ( [7, 7, 2, 2, 10, 10, 10], 7),
    ([], None),
    ([5], None),
    ([-1, -2, -3], -2),
    ([float('-inf'), float('-inf')], None),
]

run_tests(second_max, test_cases)
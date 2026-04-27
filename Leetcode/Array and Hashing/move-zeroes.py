import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def move_zeroes(nums):
    i = 0
    j = 0

    while i < len(nums):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

        i += 1

    for i in range(j, len(nums)):
        nums[i] = 0

    return nums

    

test_cases = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0, 0, 1], [1, 0, 0]),
]

run_tests(move_zeroes, test_cases)
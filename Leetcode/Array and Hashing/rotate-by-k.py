import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def rotate(nums, k):
    k %= len(nums)

    nums[:] = nums[-k:] + nums[:-k]

    return nums
    

test_cases = [
    (([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4]),
    (([-1,-100,3,99], 2), [3,99,-1,-100]),
]

run_tests(rotate, test_cases)
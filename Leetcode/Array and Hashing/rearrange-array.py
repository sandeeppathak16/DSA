import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def rearrange_array(nums):
    n = len(nums)
    ans = [0] * n

    positiveIndex = 0
    negativeIndex = 1

    for num in nums:
        if num < 0:
            ans[negativeIndex] = num
            negativeIndex += 2

        else:
            ans[positiveIndex] = num
            positiveIndex += 2

    return ans

test_cases = [
    ([3,1,-2,-5,2,-4], [3,-2,1,-5,2,-4]),
    ([-1,1], [1, -1]),
]

run_tests(rearrange_array, test_cases)
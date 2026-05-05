import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def max_sub_array(nums):
    max_sum = float('-inf')
    cc = 0
    i = 0

    ans = []

    for j, num in enumerate(nums):
        if num >= 0:
            cc += num
            if cc > max_sum or (cc == max_sum and num == 0):
                cc = max_sum
                ans = nums[i:j+1]
        else:
            cc = 0
            i = j + 1

    
    if not ans:
        return [-1]
    
    return ans
    
    

test_cases = [
    ([1, 2, 3], [1, 2, 3]),
    ([-1, 2], [2]),
    ([2], [2]),
    ([-1, -2], [-1]),
]

run_tests(max_sub_array, test_cases)
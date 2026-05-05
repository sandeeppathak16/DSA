import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def mejority_element(nums):
    cc = 0
    ce = None

    for num in nums:
        if cc == 0:
            cc = 1
            ce = num
        elif ce == num:
            cc += 1
        else:
            cc -= 1

    return ce 
    
    
    

test_cases = [
    ([2,2,1], 2),
    ([3,2,3], 3),
    ([2,2,1,1,1,2,2], 2),
]

run_tests(mejority_element, test_cases)
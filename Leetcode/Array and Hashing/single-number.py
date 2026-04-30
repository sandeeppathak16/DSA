import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def single_number(nums):
    xor = 0

    for num in nums:
        xor ^= num

    return xor
    
    

test_cases = [
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1),
]

run_tests(single_number, test_cases)
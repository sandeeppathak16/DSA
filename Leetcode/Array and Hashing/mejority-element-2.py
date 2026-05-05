import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def mejority_element(nums):
    if len(nums) <= 2:
        return list(set(nums))
    
    c1, c2 = 0, 0
    e1, e2 = None, None

    for num in nums:
        if c1 == 0 and num != e2:
            c1 = 1
            e1 = num
        elif c2 == 0 and num != e1:
            c2 = 1
            e2 = num
        elif num == e1:
            c1 += 1
        elif num == e2:
            c2 += 1
        else:
            c1 -= 1
            c2 -= 1

    
    ans = []

    c1, c2 = 0, 0

    for num in nums:
        if num == e1:
            c1 += 1
        elif num == e2:
            c2 += 1

    
    mini = int(len(nums)/ 3) + 1

    if c1 >= mini:
        ans.append(e1)

    if c2 >= mini:
        ans.append(e2)

    return ans

    

test_cases = [
    ([3, 2, 3], [3]),
    ([1, 1, 1, 3, 3, 2, 2, 2], [1, 2]),
    ([1, 2, 3, 4], []),
    ([1, 2, 3, 1, 2, 3], []),
    ([1, 1, 1, 2, 2, 3], [1]),
    ([5, 5, 5, 5], [5]),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([-1, -1, -1, 2, 3], [-1]),
    ([2,2,9,3,9,3,9,3,9,3,9,3,9], [3, 9]),
]
run_tests(mejority_element, test_cases)
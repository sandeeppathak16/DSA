import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1

        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1
    

test_cases = [
    (([4,5,6,7,0,1,2], 0,), 4),
    (([4,5,6,7,0,1,2], 3,), -1),
    (([1], 3,), -1),
]

run_tests(search, test_cases)
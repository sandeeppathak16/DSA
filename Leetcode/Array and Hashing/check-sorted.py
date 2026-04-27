import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def check(nums):
    n = len(nums)

    def check_non_decreasing(nums, n):
        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                continue

            else:
                return False

        return True

    if check_non_decreasing(nums, n):
        return True

    pick_indx = None

    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            pick_indx = i
            break

    if not pick_indx:
        return False


    return check_non_decreasing(nums[pick_indx:] + nums[:pick_indx], n)
    

test_cases = [
    ([3,4,5,1,2], True),
    ([2,1,3,4], False),
    ([1,2,3], True),
]

run_tests(check, test_cases)
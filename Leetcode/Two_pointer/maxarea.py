import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def maxarea(height):
    l = 0
    r = len(height) - 1
    ans = 0

    while l < r:
        minh = min(height[l], height[r])
        area = minh * (r - l)
        ans = max(ans, area)

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    
    return ans



test_cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
]

run_tests(maxarea, test_cases)
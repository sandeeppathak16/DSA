import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests



def trap(height):
    l, r = 0, len(height) - 1
    lmax, rmax = height[l], height[r]
    ans = 0

    while l < r:
        if lmax < rmax:
            l += 1
            lmax = max(lmax, height[l])
            ans += (lmax - height[l])
        else:
            r -= 1
            rmax = max(rmax, height[r])
            ans += (rmax - height[r])

    
    return ans



test_cases = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
]

run_tests(trap, test_cases)
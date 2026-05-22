import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests

def mySqrt(x):
    if x == 0:
        return x
    
    l = 1
    r = x // 2

    ans = 1

    while l <= r:
        m = (l + r) // 2

        if m * m <= x:
            ans = m
            l = m + 1

        else:
            r = m - 1

    
    return ans

        

    

test_cases = [
    ((0,), 0),
    ((1,), 1),
    ((4,), 2),
    ((8,), 2),
    ((9,), 3),
    ((15,), 3),
    ((16,), 4),
    ((24,), 4),
    ((25,), 5),
]

run_tests(mySqrt, test_cases)

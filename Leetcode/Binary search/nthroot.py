import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def nthRoot(n, m):
    l = 1
    r = m

    while l <= r:
        mid = (l + r) // 2

        value = mid ** n

        if value == m:
            return mid
        
        elif value < m:
            l = mid + 1

        else:
            r = mid - 1

    return -1
    

        
    

test_cases = [
    ((2, 16), 4),
    ((3, 27), 3),
    ((3, 64), 4),
    ((2, 10), -1),
    ((4, 69), -1),
    ((1, 7), 7),
]

run_tests(nthRoot, test_cases)

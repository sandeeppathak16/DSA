import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def min_day(bloom_day, m, k):
    val = m * k

    n = len(bloom_day)

    if val > n:
        return -1
    
    l = min(bloom_day)
    r = max(bloom_day)

    while l <= r:
        mid = (l + r) // 2

        cnt = 0
        nob = 0

        for i in range(n):
            if bloom_day[i] <= mid:
                cnt += 1
            else:
                nob += (cnt // k)
                cnt = 0

        
        nob += (cnt // k)

        if nob >= m:
            r = mid - 1
        else:
            l = mid + 1

    return l

        
    
    

test_cases = [
    (([1,10,3,10,2], 3, 1), 3),
    (([1,10,3,10,2], 3, 2), -1),
    (([7,7,7,7,12,7,7], 2, 3), 12),
    (([1000000000,1000000000], 1, 1), 1000000000),
    (([1,10,2,9,3,8,4,7,5,6], 4, 2), 9),
]

run_tests(min_day, test_cases)
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def sum_sub_array_min(arr):
    n = len(arr)

    prev_smaller = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)

    
    next_smaller = [n] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        next_smaller[i] = stack[-1] if stack else n
        stack.append(i)

    MOD = 10 ** 9 + 7

    ans = 0

    for i in range(n):
        left = i - prev_smaller[i]
        right = next_smaller[i] - i

        ans += (arr[i] * left * right)

    return ans % MOD
    
    

test_cases = [
    ([3,1,2,4], 17),
    ([5], 5),
    ([2,2], 6),
    ([2,2,2], 12),
    ([1,2,3,4], 20),
    ([4,3,2,1], 20),
    ([1,1,2], 7),
    ([5,1,5], 14),
    ([71,55,82,55], 593),
    ([11,81,94,43,3], 444),
]

run_tests(sum_sub_array_min, test_cases)
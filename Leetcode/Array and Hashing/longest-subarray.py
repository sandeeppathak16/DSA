import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def longest_subarray(nums, k):
    prefix_sum = {}
    current_sum = 0
    ans = 0

    for i, num in enumerate(nums):
        current_sum += num


        if current_sum == k:
            ans = i + 1

        rem = k - current_sum

        if rem in prefix_sum:
            ans = max(ans, i - current_sum[rem])

        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return ans
    


test_cases = [
    (( [10, 5, 2, 7, 1, -10], 15,), 6),
    (([-5, 8, -14, 2, 4, 12], -5), 5),
    (([10, -10, 20, 30], 5), 0),
]

run_tests(longest_subarray, test_cases)
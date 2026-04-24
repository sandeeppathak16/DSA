import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0 for _ in range(n)]
    stack = []

    for i, t in enumerate(temperatures):
        while stack and stack[-1][1] < t:
            ans[stack[-1][0]] = i - stack[-1][0]
            stack.pop()

        stack.append([i, t])

    return ans


test_cases = [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0]),
]

run_tests(daily_temperatures, test_cases)
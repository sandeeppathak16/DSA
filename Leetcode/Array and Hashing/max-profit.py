import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def maxProfit(prices):
    max_profit = float('-inf')
    buy = prices[0]

    for p in prices:
        if buy > p:
            buy = p

        max_profit = max(max_profit, p - buy)

    return max_profit    

test_cases = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
]

run_tests(maxProfit, test_cases)
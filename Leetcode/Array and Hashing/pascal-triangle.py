import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def generate(numRows):
    def generateRow(row):
        ans = 1
        ansRow = [1]

        for col in range(1, row):
            ans *= (row - col)
            ans //= col
            ansRow.append(ans)

        return ansRow
    
    ans = []

    for row in range(1, numRows + 1):
        ans.append(generateRow(row=row))

    return ans

    

test_cases = [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]]),
]

run_tests(generate, test_cases)
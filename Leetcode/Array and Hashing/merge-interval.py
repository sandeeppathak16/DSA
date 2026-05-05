
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def merge(intervals):
    if not intervals:
        return []
    
    intervals = sorted(intervals, key= lambda items: items[0])

    ans = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        else:
            ans.append(intervals[i])

    return ans



test_cases = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[1,2],[3,4],[5,6]], [[1,2],[3,4],[5,6]]),
    ([[1,5]], [[1,5]]),
    ([[1,10],[2,3],[4,8]], [[1,10]]),
    ([[5,7],[1,3],[2,4]], [[1,4],[5,7]]),
]

run_tests(merge, test_cases)
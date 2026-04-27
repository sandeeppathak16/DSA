import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def car_fleet(target, position, speed):
    car = sorted(zip(position, speed), reverse=True)
    stack = []

    for p, s in car:
        t = (target - p) // s

        stack.append(t)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    
    return len(stack)


test_cases = [
    ((12, [10,8,0,5,3], [2,4,1,1,3],), 3),
    ((10, [3], [3],), 1),
    ((100, [0,2,4], [4,2,1],), 1),
]

run_tests(car_fleet, test_cases)
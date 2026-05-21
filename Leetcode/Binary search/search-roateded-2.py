import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def search(nums, target):
     


    

test_cases = [
    # Basic rotated array
    (([4,5,6,7,0,1,2], 0,), True),
    (([4,5,6,7,0,1,2], 3,), False),

    # Single element
    (([1], 1,), True),
    (([1], 3,), False),

    # Duplicates present
    (([2,5,6,0,0,1,2], 0,), True),
    (([2,5,6,0,0,1,2], 3,), False),

    # All duplicates
    (([1,1,1,1,1], 1,), True),
    (([1,1,1,1,1], 2,), False),

    # Rotation with duplicates
    (([1,0,1,1,1], 0,), True),
    (([1,1,1,0,1], 0,), True),

    # Target at boundaries
    (([3,1,1], 3,), True),
    (([1,1,3,1], 3,), True),

    # No rotation
    (([1,2,3,4,5,6], 4,), True),
    (([1,2,3,4,5,6], 7,), False),

    # Two elements
    (([3,1], 1,), True),
    (([3,1], 3,), True),
    (([3,1], 0,), False),

    # Edge duplicate cases
    (([1,1,1,1,3,1], 3,), True),
    (([1,3,1,1,1], 3,), True),
]

run_tests(search, test_cases)
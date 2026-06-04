import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from testcase import run_tests


def asteroid_collision(asteroids):
    stack = []

    for asteroid in asteroids:
        alive = True

        while alive and asteroid < 0 and stack and stack[-1] > 0:
            if stack[-1] < -asteroid:
                stack.pop()

            elif stack[-1] == -asteroid:
                stack.pop()
                alive = False
            
            else:
                alive = False

        
        if alive:
            stack.append(asteroid)

    
    return stack
    
    
    

test_cases = [
    # No collisions
    ([1, 2, 3], [1, 2, 3]),
    ([-1, -2, -3], [-1, -2, -3]),

    # Simple collision
    ([5, 10, -5], [5, 10]),

    # Equal size collision
    ([8, -8], []),

    # Larger negative survives
    ([10, 2, -5], [10]),

    # Negative destroys multiple positives
    ([1, 2, 3, -10], [-10]),

    # Multiple collisions
    ([10, 2, -5, -15], [-15]),

    # Asteroids moving away from each other
    ([-2, 1], [-2, 1]),

    # Chain reaction
    ([4, 3, 2, -10], [-10]),

    # Equal collision after popping smaller ones
    ([5, 1, -5], []),

    # Mixed example
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),

    # LeetCode example
    ([-2, -2, 1, -2], [-2, -2, -2]),

    # Single asteroid
    ([5], [5]),
    ([-5], [-5]),

    # Empty result
    ([1, -1], []),

    # Larger positive survives
    ([20, 5, -10], [20]),

    # Multiple equal collisions
    ([3, 5, -5, -3], []),

    # Complex chain
    ([1, -2, -2, -2], [-2, -2, -2]),

    # Another chain
    ([2, -1, -2], []),

    # Negative arrives after several positives
    ([1, 2, 3, 4, -3], [1, 2, 3, 4]),

    # Large negative wipes everything
    ([1, 2, 3, 4, -20], [-20]),
]
run_tests(asteroid_collision, test_cases)
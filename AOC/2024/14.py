import re
from math import lcm

WIDTH = 101
HEIGHT = 103

with open("14.txt") as f:
    robots = [
        tuple(map(int, re.findall(r"-?\d+", line)))
        for line in f
    ]


def get_positions(t):
    return [
        (
            (x + vx * t) % WIDTH,
            (y + vy * t) % HEIGHT,
        )
        for x, y, vx, vy in robots
    ]


def solve(part):
    if part == 1:
        pts = get_positions(100)

        mid_x = WIDTH // 2
        mid_y = HEIGHT // 2

        q1 = q2 = q3 = q4 = 0

        for x, y in pts:
            if x == mid_x or y == mid_y:
                continue

            if x < mid_x and y < mid_y:
                q1 += 1
            elif x > mid_x and y < mid_y:
                q2 += 1
            elif x < mid_x and y > mid_y:
                q3 += 1
            else:
                q4 += 1

        return q1 * q2 * q3 * q4

    if part == 2:
        cycle = lcm(WIDTH, HEIGHT)

        best_score = -1
        best_time = 0

        for t in range(cycle):
            pts = set(get_positions(t))

            score = 0

            for x, y in pts:
                if (x + 1, y) in pts:
                    score += 1
                if (x, y + 1) in pts:
                    score += 1

            if score > best_score:
                best_score = score
                best_time = t

        return best_time


print("Part 1:", solve(1))
print("Part 2:", solve(2))
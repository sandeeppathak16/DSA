import re

WIDTH = 101
HEIGHT = 103
TIME = 100

with open("14.txt") as f:
    lines = f.readlines()

robots = []

for line in lines:
    nums = list(map(int, re.findall(r"-?\d+", line)))
    x, y, vx, vy = nums
    robots.append((x, y, vx, vy))

# mid_x = WIDTH // 2
# mid_y = HEIGHT // 2
#
# q1 = q2 = q3 = q4 = 0
#
# for x, y, vx, vy in robots:
#     nx = (x + vx * TIME) % WIDTH
#     ny = (y + vy * TIME) % HEIGHT
#
#     if nx == mid_x or ny == mid_y:
#         continue
#
#     if nx < mid_x and ny < mid_y:
#         q1 += 1
#     elif nx > mid_x and ny < mid_y:
#         q2 += 1
#     elif nx < mid_x and ny > mid_y:
#         q3 += 1
#     elif nx > mid_x and ny > mid_y:
#         q4 += 1
#
# print(q1, q2, q3, q4)
# print("Safety Factor =", q1 * q2 * q3 * q4)


def positions_at(t):
    pts = []
    for x, y, vx, vy in robots:
        nx = (x + vx * t) % WIDTH
        ny = (y + vy * t) % HEIGHT
        pts.append((nx, ny))
    return pts


best_time = None
best_area = float("inf")

for t in range(1, 20000):
    pts = positions_at(t)
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    area = (max(xs) - min(xs)) * (max(ys) - min(ys))

    if area < best_area:
        best_area = area
        best_time = t

print("Easter egg appears at:", best_time)

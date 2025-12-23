from itertools import combinations
from math import gcd

with open('8.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

R = len(grid)
C = len(grid[0])

antennas = {}
for r in range(R):
    for c in range(C):
        ch = grid[r][c]
        if ch != '.':
            antennas.setdefault(ch, []).append((r, c))

antinodes = set()

for freq, points in antennas.items():
    for (r1, c1), (r2, c2) in combinations(points, 2):
        dr = r2 - r1
        dc = c2 - c1

        p1 = (r1 - dr, c1 - dc)
        p2 = (r2 + dr, c2 + dc)

        for r, c in (p1, p2):
            if 0 <= r < R and 0 <= c < C:
                antinodes.add((r, c))

print(len(antinodes))

antinodes = set()


def in_bounds(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


for freq, points in antennas.items():
    if len(points) < 2:
        continue

    antinodes.update(points)

    for (r1, c1), (r2, c2) in combinations(points, 2):
        dr = r2 - r1
        dc = c2 - c1

        g = gcd(dr, dc)
        dr //= g
        dc //= g

        r, c = r1 + dr, c1 + dc
        while in_bounds(r, c):
            antinodes.add((r, c))
            r += dr
            c += dc

        r, c = r1 - dr, c1 - dc
        while in_bounds(r, c):
            antinodes.add((r, c))
            r -= dr
            c -= dc

print(len(antinodes))

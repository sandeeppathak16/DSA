from collections import deque
from itertools import permutations


def solve(filename="24.txt", part_2=False):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    start = None
    points = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c].isdigit():
                if grid[r][c] == "0":
                    start = (r, c)
                else:
                    points.append((r, c))

    all_nodes = [start] + points

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    node_distance = {}

    for i, src in enumerate(all_nodes):
        for j, dst in enumerate(all_nodes):
            if i >= j:
                continue

            q = deque([(src, 0)])
            visited = {src}

            min_steps = None

            while q:
                (x, y), steps = q.popleft()

                if (x, y) == dst:
                    min_steps = steps
                    break

                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if not (0 <= new_x < rows and 0 <= new_y < cols):
                        continue

                    if (new_x, new_y) in visited:
                        continue

                    if grid[new_x][new_y] == "#":
                        continue

                    if part_2 and grid[new_x][new_y] == '0':
                        continue

                    visited.add((new_x, new_y))
                    q.append(((new_x, new_y), steps + 1))

            node_distance[(src, dst)] = min_steps
            node_distance[(dst, src)] = min_steps

    answer = float("inf")

    for perm in permutations(points):
        prev = start
        total_steps = 0

        for p in perm:
            total_steps += node_distance[(prev, p)]
            prev = p

        if part_2:
            total_steps += node_distance[(prev, start)]

        answer = min(answer, total_steps)

    return answer


print(solve(part_2=True))
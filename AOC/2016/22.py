import re
from collections import deque


def solve(filename="22.txt", part_1=True):
    pattern = re.compile(
        r"^/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%$"
    )

    nodes = []
    with open(filename) as f:
        for line in f:
            match = pattern.match(line)
            if match:
                nodes.append(tuple(map(int, match.groups())))

    if part_1:
        nodes.sort(key=lambda node: node[5], reverse=True)

        ans = 0

        for i, node in enumerate(nodes):
            used = node[3]
            j = len(nodes) - 1

            while 0 <= j != i and nodes[j][4] >= used:
                j -= 1

            ans += len(nodes) - 1 - j

        return ans

    max_x = max(x for x, _, *_ in nodes)
    max_y = max(y for _, y, *_ in nodes)

    grid = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    empty_size = next(size for _, _, size, used, *_ in nodes if used == 0)

    empty = None

    for x, y, size, used, *_ in nodes:
        if used == 0:
            empty = (y, x)
            grid[y][x] = "_"
        elif used > empty_size:
            grid[y][x] = "#"

    goal = (0, max_x)
    target = (0, max_x - 1)

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    queue = deque([(empty, 0)])
    visited = {empty}

    while queue:
        (y, x), steps = queue.popleft()

        if (y, x) == target:
            return steps + 5 * (max_x - 1) + 1

        for dy, dx in directions:
            new_y = y + dy
            new_x = x + dx

            if not (0 <= new_y <= max_y and 0 <= new_x <= max_x):
                continue

            if (new_y, new_x) in visited:
                continue

            if grid[new_y][new_x] == "#" or (new_y, new_x) == goal:
                continue

            visited.add((new_y, new_x))
            queue.append(((new_y, new_x), steps + 1))


print(solve(part_1=True))
from collections import deque


def solve(filename="20.txt", cheat_len=20):
    with open(filename) as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0])

    start = end = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)

    queue = deque([start])
    parent = {start: None}

    while queue:
        r, c = queue.popleft()

        if (r, c) == end:
            break

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] != "#"
                and (nr, nc) not in parent
            ):
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

    path = []
    cur = end

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    distance = {pos: idx for idx, pos in enumerate(path)}

    count = 0

    for pos in path:
        start_idx = distance[pos]
        r, c = pos

        for dr in range(-cheat_len, cheat_len + 1):
            remaining = cheat_len - abs(dr)

            for dc in range(-remaining, remaining + 1):
                cheat_dist = abs(dr) + abs(dc)

                if cheat_dist == 0:
                    continue

                target = (r + dr, c + dc)

                if target not in distance:
                    continue

                saving = (
                    distance[target]
                    - start_idx
                    - cheat_dist
                )

                if saving >= 100:
                    count += 1

    return count


print("Part 1:", solve(cheat_len=2))
print("Part 2:", solve(cheat_len=20))
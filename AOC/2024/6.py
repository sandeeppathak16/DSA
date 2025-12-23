with open("6.txt") as f:
    grid = [list(line.strip()) for line in f]

ROWS, COLS = len(grid), len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] in "^v<>":
            start = (r, c)
            start_dir = {
                "^": (-1, 0),
                "v": (1, 0),
                "<": (0, -1),
                ">": (0, 1),
            }[grid[r][c]]
            break

TURN = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}


visited = set()
r, c = start
direction = start_dir

while 0 <= r < ROWS and 0 <= c < COLS:
    visited.add((r, c))
    dr, dc = direction
    nr, nc = r + dr, c + dc

    if not (0 <= nr < ROWS and 0 <= nc < COLS):
        break

    if grid[nr][nc] == "#":
        direction = TURN[direction]
    else:
        r, c = nr, nc

print("Part 1:", len(visited))


def causes_loop(block_r, block_c):
    r, c = start
    direction = start_dir
    seen = set()

    while 0 <= r < ROWS and 0 <= c < COLS:
        state = (r, c, direction)
        if state in seen:
            return True
        seen.add(state)

        dr, dc = direction
        nr, nc = r + dr, c + dc

        if not (0 <= nr < ROWS and 0 <= nc < COLS):
            return False

        if (nr, nc) == (block_r, block_c) or grid[nr][nc] == "#":
            direction = TURN[direction]
        else:
            r, c = nr, nc

    return False


count = 0
for r, c in visited:
    if (r, c) == start:
        continue
    if causes_loop(r, c):
        count += 1

print("Part 2:", count)

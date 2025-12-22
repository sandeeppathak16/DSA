with open('6.txt', 'r') as f:
    grids = [line.strip() for line in f.readlines()]

seen = set()
guard_position = None
row = len(grids)
col = len(grids[0])
direction = None

for r in range(row):
    if guard_position:
        break

    for c in range(col):
        if grids[r][c] == '^':
            guard_position = (r, c)
            direction = (-1, 0)
        elif grids[r][c] == 'v':
            guard_position = (r, c)
            direction = (1, 0)
        elif grids[r][c] == '<':
            guard_position = (r, c)
            direction = (0, -1)
        elif grids[r][c] == '>':
            guard_position = (r, c)
            direction = (0, 1)

turn_mapping = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

r, c = guard_position

ans1 = 0
while r < row and c < col:
    if (r, c) not in seen:
        seen.add((r, c))
        ans1 += 1

    x, y = direction
    rx, cy = r + x, c + y
    if rx >= row or cy >= col or rx < 0 or cy < 0:
        break

    if grids[rx][cy] == '#':
        direction = turn_mapping[direction]
        continue

    r = rx
    c = cy

print(ans1)







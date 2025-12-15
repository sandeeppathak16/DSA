from collections import deque

coords = set()

maxRow, maxCol = float('-inf'), float('-inf')

with open("9dec.txt") as f:
    for line in f:
        y, x = map(int, line.strip().split(","))
        maxRow = max(x, maxRow)
        maxCol = max(y, maxCol)
        coords.add((x, y))

grids = []
for row in range(maxRow + 1):
    grid = []
    for col in range(maxCol + 1):
        if (row, col) in coords:
            grid.append('#')
        else:
            grid.append('.')

    grids.append(grid)

for g in grids:
    print("".join(g))

maxArea = float('-inf')
for row in range(maxRow + 1):
    for col in range(maxCol + 1):
        if grids[row][col] == '.':
            continue

        x1, y1 = row, col
        while x1 < maxRow and y1 < maxCol:
            if grids[x1 + 1][y1 + 1] == '#':
                area = (y1 + 1 - col) * (x1 + 1 - row)
                maxArea = max(maxArea, area)
                # print(area, (row, col), (x1, y1))

            x1 += 1
            y1 += 1

        x2, y2 = row, col
        while y2 > 0 and x2 < maxRow:
            if grids[x2 + 1][y2 - 1] == '#':
                area = (col - (y2 - 1)) * (x2 + 1 - row)
                maxArea = max(maxArea, area)

            x2 += 1
            y2 -= 1

        x3, y3 = row, col
        while y3 < maxCol and x3 > 0:
            if grids[x3 - 1][y3 + 1] == '#':
                area = ((y3 + 1) - col) * (row - (x3 - 1))
                maxArea = max(maxArea, area)

            x3 -= 1
            y3 += 1

        x4, y4 = row, col
        while y4 > 0 and x4 > 0:
            if grids[x4 - 1][y4 - 1] == '#':
                area = (col - (y4 - 1)) * (row - (x4 - 1))
                maxArea = max(maxArea, area)

            x4 -= 1
            y4 -= 1

print(maxArea)

coords = list(coords)

maxArea = 0

for i in range(len(coords)):
    x1, y1 = coords[i]
    for j in range(i + 1, len(coords)):
        x2, y2 = coords[j]

        if x1 == x2 or y1 == y2:
            continue

        c3 = (x1, y2)
        c4 = (x2, y1)

        if c3 in coords and c4 in coords:
            width = abs(y2 - y1) + 1
            height = abs(x2 - x1) + 1
            area = width * height
            maxArea = max(maxArea, area)

print(maxArea)

reds = []
with open("9dec.txt") as f:
    for line in f:
        y, x = map(int, line.strip().split(","))
        reds.append((x, y))

max_x = max(r[0] for r in reds)
max_y = max(r[1] for r in reds)

W, H = max_y + 1, max_x + 1

grid = [[0] * W for _ in range(H)]

for x, y in reds:
    grid[x][y] = 2

n = len(reds)
for i in range(n):
    (x1, y1) = reds[i]
    (x2, y2) = reds[(i + 1) % n]

    if x1 == x2:
        step = 1 if y2 > y1 else -1
        for y in range(y1, y2 + step, step):
            if grid[x1][y] == 0:
                grid[x1][y] = 1
    else:
        step = 1 if x2 > x1 else -1
        for x in range(x1, x2 + step, step):
            if grid[x][y1] == 0:
                grid[x][y1] = 1

visited = [[False] * W for _ in range(H)]
q = deque()

for x in range(H):
    for y in [0, W - 1]:
        if grid[x][y] == 0:
            q.append((x, y))
            visited[x][y] = True

for y in range(W):
    for x in [0, H - 1]:
        if grid[x][y] == 0:
            q.append((x, y))
            visited[x][y] = True

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

for x in range(H):
    for y in range(W):
        if grid[x][y] == 0 and not visited[x][y]:
            grid[x][y] = 1

reds = list(set(reds))
maxArea = 0


def rect_ok(x1, y1, x2, y2):
    xmin, xmax = sorted([x1, x2])
    ymin, ymax = sorted([y1, y2])
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            if grid[x][y] == 0:
                return False
    return True


for i in range(len(reds)):
    x1, y1 = reds[i]
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]

        if x1 == x2 or y1 == y2:
            continue

        if rect_ok(x1, y1, x2, y2):
            area = abs(x2 - x1) + 1
            area *= abs(y2 - y1) + 1
            maxArea = max(maxArea, area)

print(maxArea)
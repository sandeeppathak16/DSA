with open('10.txt', 'r') as file:
    grid = []
    for line in file.readlines():
        grid.append([int(c) for c in line.strip()])

ROW = len(grid)
COL = len(grid[0])

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

ans2 = 0


def travel(i, j, reachable):
    global ans2

    if grid[i][j] == 9:
        reachable.add((i, j))
        ans2 += 1
        return

    for di, dj in dirs:
        ni, nj = i + di, j + dj

        if 0 <= ni < ROW and 0 <= nj < COL:
            if grid[ni][nj] - grid[i][j] == 1:
                travel(ni, nj, reachable)


ans1 = 0

for r in range(ROW):
    for c in range(COL):
        if grid[r][c] == 0:
            reachable = set()
            travel(r, c, reachable)
            ans1 += len(reachable)

print(ans1, ans2)

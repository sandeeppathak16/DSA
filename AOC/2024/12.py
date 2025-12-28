with open('12.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

ROW = len(grid)
COL = len(grid[0])

visited = [[False for _ in range(COL)] for _ in range(ROW)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def travel(i, j):
    visited[i][j] = True
    area = 1
    perimeter = 4

    for di, dj in dirs:
        ni, nj = i + di, j + dj

        if 0 <= ni < ROW and 0 <= nj < COL:
            if grid[i][j] == grid[ni][nj]:
                perimeter -= 1
                if not visited[ni][nj]:
                    a, p = travel(ni, nj)
                    area += a
                    perimeter += p

    return area, perimeter


ans1 = 0
for r in range(ROW):
    for c in range(COL):
        if not visited[r][c]:
            area, perimeter = travel(r, c)
            ans1 += (area * perimeter)


print(ans1)


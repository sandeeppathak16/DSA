with open('4.txt', 'r') as f:
    grid = [line.strip() for line in f.readlines()]


row = len(grid)
col = len(grid[0])
check = {'XMAS', 'SAMX'}

ans1 = 0
for r in range(row):
    for c in range(col):

        if grid[r][c] not in {'X', 'S'}:
            continue

        if c + 4 <= col and grid[r][c:c+4] in check:
            ans1 += 1

        if r + 4 <= row:
            w = ''
            for i in range(r, r + 4):
                w += grid[i][c]

            if w in check:
                ans1 += 1

        if r + 4 <= row and c + 4 <= col:
            i, j = r, c
            w = ''
            while i < r + 4 and j < c + 4:
                w += grid[i][j]
                i += 1
                j += 1

            if w in check:
                ans1 += 1

        if r + 4 <= row and c >= 3:
            i, j = r, c
            w = ''
            while i < r + 4 and j >= 0:
                w += grid[i][j]
                i += 1
                j -= 1

            if w in check:
                ans1 += 1

print(ans1)

ans2 = 0
check = {'SAM', 'MAS'}
for r in range(0, row - 2):
    for c in range(2, col):
        if grid[r][c] not in {'M', 'S'} or grid[r][c - 2] not in {'M', 'S'}:
            continue

        i, j = r, c - 2

        w = ''
        while i < i + 3 and j <= c:
            w += grid[i][j]
            i += 1
            j += 1

        if w not in check:
            continue

        i, j = r, c

        w = ''
        while i < i + 3 and j >= c - 2:
            w += grid[i][j]
            i += 1
            j -= 1

        if w not in check:
            continue

        ans2 += 1


print(ans2)
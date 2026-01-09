with open('16.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]


source = None
target = None

ROWS = len(grid)
COLS = len(grid[0])


for r in range(ROWS):
    if source and target:
        break

    for c in range(COLS):
        if grid[r][c] == 'S':
            source = (r, c)

        if grid[r][c] == 'E':
            target = (r, c)


print(source, target)
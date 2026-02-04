grid = []
with open("11.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

galaxies = []
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '#':
            galaxies.append((r, c))

empty_rows = set()
for r in range(rows):
    if '#' not in grid[r]:
        empty_rows.add(r)

empty_cols = set()
for c in range(cols):
    if all(grid[r][c] == '.' for r in range(rows)):
        empty_cols.add(c)

total = 0
n = len(galaxies)

for i in range(n):
    r1, c1 = galaxies[i]
    for j in range(i + 1, n):
        r2, c2 = galaxies[j]

        dist = abs(r1 - r2) + abs(c1 - c2)

        for r in empty_rows:
            if min(r1, r2) < r < max(r1, r2):
                dist += 1000000 - 1

        for c in empty_cols:
            if min(c1, c2) < c < max(c1, c2):
                dist += 1000000 - 1

        total += dist

print(total)

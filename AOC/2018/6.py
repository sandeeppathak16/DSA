with open("6.txt", "r") as f:
    points = []
    for line in f:
        x, y = map(int, line.strip().split(", "))
        points.append((x, y))


alpha = [str(i) for i in range(len(points))]

max_x = max(points, key=lambda x: x[0])[0]
max_y = max(points, key=lambda x: x[1])[1]

grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for i, (x, y) in enumerate(points):
    grid[y][x] = alpha[i]


for i in range(max_x + 1):
    for j in range(max_y + 1):
        if grid[j][i] == '.':
            minDistance = float('inf')
            secondMinDistance = float('inf')
            closestPoint = None
            for x, y in points:
                distance = abs(x - i) + abs(y - j)
                if distance < minDistance:
                    minDistance = distance
                    closestPoint = grid[y][x]
                elif distance <= minDistance and secondMinDistance > distance:
                    secondMinDistance = distance
            
            if secondMinDistance == minDistance:
                grid[j][i] = '#'
            else:
                grid[j][i] = closestPoint


infinites = set()
for c in range(max_x + 1):
    if grid[0][c] != '#':
        infinites.add(grid[0][c])
    if grid[max_y][c] != '#':
        infinites.add(grid[max_y][c])
for c in range(max_y + 1):
    if grid[c][0] != '#':
        infinites.add(grid[c][0])
    if grid[c][max_x] != '#':
        infinites.add(grid[c][max_x])


for i in range(max_x + 1):
    for j in range(max_y + 1):
        if grid[j][i] in infinites:
            grid[j][i] = '#'


counts = {}
for i in range(max_x + 1):
    for j in range(max_y + 1):
        if grid[j][i] != '#':
            counts[grid[j][i]] = counts.get(grid[j][i], 0) + 1

print(max(counts.values()))
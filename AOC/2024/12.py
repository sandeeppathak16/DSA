from collections import deque, defaultdict

with open('12.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

ROW = len(grid)
COL = len(grid[0])

visited = [[False for _ in range(COL)] for _ in range(ROW)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_perimeter(i, j):
    visited[i][j] = True
    area = 1
    perimeter = 4

    for di, dj in dirs:
        ni, nj = i + di, j + dj

        if 0 <= ni < ROW and 0 <= nj < COL:
            if grid[i][j] == grid[ni][nj]:
                perimeter -= 1
                if not visited[ni][nj]:
                    a, p = get_perimeter(ni, nj)
                    area += a
                    perimeter += p

    return area, perimeter


# dirs_with_side = [(1, 0, 'b'), (0, 1, 'r'), (-1, 0, 'l'), (0, -1, 't')]
# all_sides = {'b', 'r', 'l', 't'}


# def get_side(i, j):
#     visited[i][j] = True
#     area = 1
#     side_count = {
#         'l_side': 1,
#         'r_side': 1,
#         'b_side': 1,
#         't_side': 1
#     }
#     sides = set()
#     visited_side = set()
#
#     for di, dj, side in dirs_with_side:
#         ni, nj = i + di, j + dj
#
#         if 0 <= ni < ROW and 0 <= nj < COL:
#             if grid[i][j] == grid[ni][nj]:
#                 if not visited[ni][nj]:
#                     sides.add(side)
#                     a, _s = get_side(ni, nj)
#                     area += a
#
#                     for key, value in _s.items():
#                         side_count[key] += value
#                 else:
#                     visited_side.add(side)
#
#     for s1 in sides:
#         for s2 in all_sides - {s1}:
#             side_count[f'{s2}_side'] += 1
#
#     for s in visited_side:
#         side_count[f'{s}_side'] -= 1
#
#     return area, side_count

DIRS = [
    (-1, 0, "U"),
    (1, 0, "D"),
    (0, -1, "L"),
    (0, 1, "R"),
]


def count_runs(nums):
    if not nums:
        return 0
    runs = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            runs += 1
    return runs


def count_sides(boundary_edges):
    sides = 0

    # Horizontal sides (U, D)
    for d in ("U", "D"):
        rows = defaultdict(list)
        for dir_, r, c in boundary_edges:
            if dir_ == d:
                rows[r].append(c)

        for r in rows:
            sides += count_runs(sorted(rows[r]))

    # Vertical sides (L, R)
    for d in ("L", "R"):
        cols = defaultdict(list)
        for dir_, r, c in boundary_edges:
            if dir_ == d:
                cols[c].append(r)

        for c in cols:
            sides += count_runs(sorted(cols[c]))

    return sides


def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    plant = grid[sr][sc]

    area = 0
    boundary_edges = []

    while q:
        r, c = q.popleft()
        area += 1

        for dr, dc, dname in DIRS:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < ROW and 0 <= nc < COL):
                boundary_edges.append((dname, r, c))
            elif grid[nr][nc] != plant:
                boundary_edges.append((dname, r, c))
            elif not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))

    sides = count_sides(boundary_edges)
    return area * sides


total = 0
for r in range(ROW):
    for c in range(COL):
        if not visited[r][c]:
            total += bfs(r, c)

print(total)



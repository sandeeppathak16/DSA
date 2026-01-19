import heapq

with open('16.txt', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]


# source = None
# target = None
#
# ROWS = len(grid)
# COLS = len(grid[0])
#
# for r in range(ROWS):
#     if source and target:
#         break
#
#     for c in range(COLS):
#         if grid[r][c] == 'S':
#             source = (r, c)
#
#         if grid[r][c] == 'E':
#             target = (r, c)
#
# print(source, target)
#
# turn_mapping = {
#     (-1, 0): {  # up
#         'c': (0, 1),
#         'a': (0, -1)
#     },
#     (0, 1): {  # right
#         'c': (1, 0),
#         'a': (-1, 0)
#     },
#     (1, 0): {  # down
#         'c': (0, -1),
#         'a': (0, 1)
#     },
#     (0, -1): {  # left
#         'c': (-1, 0),
#         'a': (1, 0)
#     }
# }
#
# memo = {}
#
#
# def dfs(i, j, target, score, direction):
#     if i < 0 or j < 0 or i >= ROWS or j >= COLS:
#         return float('inf')
#
#     if (i, j) == target:
#         return score
#
#     state = (i, j, direction)
#
#     if state in memo and memo[state] <= score:
#         return float('inf')
#
#     memo[state] = score
#
#     best = float('inf')
#
#     dx, dy = direction
#     ni, nj = i + dx, j + dy
#     if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] == '.':
#         best = min(best, dfs(ni, nj, target, score + 1, direction))
#
#     for new_dir in turn_mapping[direction].values():
#         dx, dy = new_dir
#         ni, nj = i + dx, j + dy
#
#         if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] == '.':
#             best = min(
#                 best,
#                 dfs(ni, nj, target, score + 1000, new_dir)
#             )
#
#     return best
#
#
# i, j = source


# print(dfs(i, j, target, 0, (-1, 0)))

def solve(grid):
    ROWS, COLS = len(grid), len(grid[0])

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 'S':
                sr, sc = i, j
            if grid[i][j] == 'E':
                er, ec = i, j

    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W

    INF = float('inf')
    dist = [[[INF] * 4 for _ in range(COLS)] for _ in range(ROWS)]

    pq = []
    dist[sr][sc][1] = 0  # start facing East
    heapq.heappush(pq, (0, sr, sc, 1))

    while pq:
        cost, r, c, d = heapq.heappop(pq)

        if cost > dist[r][c][d]:
            continue

        # reached end
        if (r, c) == (er, ec):
            return cost

        dr, dc = DIRS[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != '#':
            if dist[nr][nc][d] > cost + 1:
                dist[nr][nc][d] = cost + 1
                heapq.heappush(pq, (cost + 1, nr, nc, d))

        for nd in [(d + 1) % 4, (d - 1) % 4]:
            if dist[r][c][nd] > cost + 1000:
                dist[r][c][nd] = cost + 1000
                heapq.heappush(pq, (cost + 1000, r, c, nd))


# print(solve(grid))

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, E, S, W
INF = float('inf')


def dijkstra(grid, start_states):
    R, C = len(grid), len(grid[0])
    dist = [[[INF] * 4 for _ in range(C)] for _ in range(R)]
    pq = []

    for r, c, d in start_states:
        dist[r][c][d] = 0
        heapq.heappush(pq, (0, r, c, d))

    while pq:
        cost, r, c, d = heapq.heappop(pq)
        if cost > dist[r][c][d]:
            continue

        # move forward
        dr, dc = DIRS[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != '#':
            if dist[nr][nc][d] > cost + 1:
                dist[nr][nc][d] = cost + 1
                heapq.heappush(pq, (cost + 1, nr, nc, d))

        # turn left / right
        for nd in [(d + 1) % 4, (d - 1) % 4]:
            if dist[r][c][nd] > cost + 1000:
                dist[r][c][nd] = cost + 1000
                heapq.heappush(pq, (cost + 1000, r, c, nd))

    return dist


def dijkstra_reverse(grid, start_states):
    R, C = len(grid), len(grid[0])
    dist = [[[INF] * 4 for _ in range(C)] for _ in range(R)]
    pq = []

    for r, c, d in start_states:
        dist[r][c][d] = 0
        heapq.heappush(pq, (0, r, c, d))

    while pq:
        cost, r, c, d = heapq.heappop(pq)
        if cost > dist[r][c][d]:
            continue

        # reverse of moving forward → move backward
        dr, dc = DIRS[d]
        pr, pc = r - dr, c - dc
        if 0 <= pr < R and 0 <= pc < C and grid[pr][pc] != '#':
            if dist[pr][pc][d] > cost + 1:
                dist[pr][pc][d] = cost + 1
                heapq.heappush(pq, (cost + 1, pr, pc, d))

        # reverse turns (same cost)
        for pd in [(d + 1) % 4, (d - 1) % 4]:
            if dist[r][c][pd] > cost + 1000:
                dist[r][c][pd] = cost + 1000
                heapq.heappush(pq, (cost + 1000, r, c, pd))

    return dist


def solve_part2(grid):
    R, C = len(grid), len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                sr, sc = r, c
            if grid[r][c] == 'E':
                er, ec = r, c

    dist_start = dijkstra(grid, [(sr, sc, 1)])

    dist_end = dijkstra_reverse(grid, [(er, ec, d) for d in range(4)])

    best = min(dist_start[er][ec])

    count = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                continue
            for d in range(4):
                if dist_start[r][c][d] + dist_end[r][c][d] == best:
                    count += 1
                    break

    return count


print(solve_part2(grid))

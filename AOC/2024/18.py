from collections import deque

_input = []
with open("18.txt", "r") as f:
    for line in f:
        x, y = line.strip().split(",")
        _input.append((int(x), int(y)))

# grid = [['.' for _ in range(71)] for _ in range(71)]

# for x, y in _input[:1024]:
#     grid[int(y)][int(x)] = '#'

# initial_position = (0, 0)
# target_position = (70, 70)

# queue = [(initial_position, 0)]
# visited = set([initial_position])

# while queue:
#     (x, y), distance = queue.pop(0)

#     if (x, y) == target_position:
#         print(distance)
#         break

#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         nx, ny = x + dx, y + dy

#         if (
#             0 <= nx < 71 and
#             0 <= ny < 71 and
#             grid[ny][nx] != '#' and
#             (nx, ny) not in visited
#         ):
#             visited.add((nx, ny))
#             queue.append(((nx, ny), distance + 1))


# grid = [['.' for _ in range(7)] for _ in range(7)]

# for x, y in _input[:12]:
#     grid[int(y)][int(x)] = '#'


# def dfs(x, y, sub_path, paths):
#     if x < 0 or x >= 7 or y < 0 or y >= 7 or grid[y][x] == '#':
#         return

#     if (x, y) == (6, 6):
#         paths.append(sub_path + [(x, y)])
#         return

#     grid[y][x] = '#'
#     sub_path.append((x, y))
#     dfs(x + 1, y, sub_path, paths)
#     dfs(x - 1, y, sub_path, paths)
#     dfs(x, y + 1, sub_path, paths)
#     dfs(x, y - 1, sub_path, paths)
#     sub_path.pop()
#     grid[y][x] = '.'

# paths = []
# dfs(0, 0, [], paths)

# for path in paths:
#     print(path)

SIZE = 71
START = (0, 0)
END = (70, 70)

def can_reach_exit(blocked):
    if START in blocked or END in blocked:
        return False

    queue = deque([START])
    visited = {START}

    while queue:
        x, y = queue.popleft()

        if (x, y) == END:
            return True

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < SIZE and
                0 <= ny < SIZE and
                (nx, ny) not in blocked and
                (nx, ny) not in visited
            ):
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False


blocked = set()

for x, y in _input:
    blocked.add((x, y))
    if not can_reach_exit(blocked):
        print(f"{x},{y}")
        break

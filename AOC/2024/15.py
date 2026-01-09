# room = []
# moves = ''
#
# with open('15.txt', 'r') as file:
#     find_moves = False
#
#     for line in file.readlines():
#         line = line.strip()
#
#         if line == '':
#             find_moves = True
#             continue
#
#         if find_moves:
#             moves += line
#             continue
#
#         room.append(list(line))
#
# move_dir = {
#     '<': (0, -1),
#     'v': (1, 0),
#     '>': (0, 1),
#     '^': (-1, 0)
# }
#
# ROWS = len(room)
# COLS = len(room[0])
# robot = None
#
# for r in range(ROWS):
#     if robot:
#         break
#
#     for c in range(COLS):
#         if room[r][c] == '@':
#             robot = (r, c)
#             break
#
# for move in moves:
#     if move not in move_dir:
#         continue
#
#     x, y = move_dir[move]
#     i, j = robot
#     ix, jy = i + x, j + y
#
#     if not (0 <= ix < ROWS and 0 <= jy < COLS):
#         continue
#
#     if room[ix][jy] == '#':
#         continue
#
#     if room[ix][jy] == '.':
#         room[i][j] = '.'
#         room[ix][jy] = '@'
#         robot = (ix, jy)
#         continue
#
#     ixx, jyy = ix + x, jy + y
#
#     while 0 <= ixx < ROWS and 0 <= jyy < COLS and room[ixx][jyy] == 'O':
#         ixx += x
#         jyy += y
#
#     if 0 <= ixx < ROWS and 0 <= jyy < COLS and room[ixx][jyy] == '.':
#         room[ixx][jyy] = 'O'
#         room[ix][jy] = '@'
#         room[i][j] = '.'
#         robot = (ix, jy)
#
# ans1 = 0
#
# for r in range(ROWS):
#     for c in range(COLS):
#         if room[r][c] == 'O':
#             ans1 += 100 * r + c
#
# print(ans1)


## not correct
# for move in moves:
#     if move not in move_dir:
#         continue
#
#     x, y = move_dir[move]
#     i, j = robot
#     ix, jy = i + x, j + y
#
#     if not (0 <= ix < NEW_ROWS and 0 <= jy < NEW_COLS):
#         continue
#
#     if room[ix][jy] == '#':
#         continue
#
#     if room[ix][jy] == '.':
#         room[i][j] = '.'
#         room[ix][jy] = '@'
#         robot = (ix, jy)
#         continue
#
#     ixx, jyy = ix + x, jy + y
#     boxs = []
#
#     if 0 <= ixx < NEW_ROWS and 0 <= jyy < NEW_COLS:
#         if move in {'^', 'v'}:
#             a, b = jyy, jyy + 1
#             while a >= 0 and new_room[ixx][a] in {'[', ']'}:
#                 a -= 1
#
#             while b < NEW_COLS and new_room[ixx][b] in {'[', ']'}:
#                 b += 1
#
#             boxs = new_room[ixx][a:b + 1]
#         else:
#             a, b = ixx, ixx + 1
#             while a >= 0 and new_room[a][jyy] in {'[', ']'}:
#                 a -= 1
#
#             while b < NEW_ROWS and new_room[b][jyy] in {'[', ']'}:
#                 b += 1
#
#             box = []
#             for z in range(a, b + 1):
#                 box.append(new_room[z][jyy])
#
#     # while boxs and '#' not in boxs and not all(for b in box)
#
#     while 0 <= ixx < NEW_ROWS and 0 <= jyy < NEW_COLS and room[ixx][jyy] in {'[', ']'}:
#         if move in {'^', 'v'}:
#             a, b = jyy, jyy + 1
#             while a >= 0 and new_room[ixx][a] in {'[', ']'}:
#                 a -= 1
#
#             while b < NEW_COLS and new_room[ixx][b] in {'[', ']'}:
#                 b += 1
#         else:
#             a, b = ixx, ixx + 1
#             while a >= 0 and new_room[a][jyy] in {'[', ']'}:
#                 a -= 1
#
#             while b < NEW_ROWS and new_room[b][jyy] in {'[', ']'}:
#                 b += 1
#
#         ixx += x
#         jyy += y
#
#     if 0 <= ixx < ROWS and 0 <= jyy < COLS and room[ixx][jyy] == '.':
#         room[ixx][jyy] = 'O'
#         room[ix][jy] = '@'
#         room[i][j] = '.'
#         robot = (ix, jy)
#
# ans2 = 0
#
# for r in range(ROWS):
#     for c in range(COLS):
#         if room[r][c] == 'O':
#             ans2 += 100 * r + c
#
# print(ans2)

# Advent of Code 2023 - Day 15 Part 2 (Correct Solution)

with open("15.txt") as f:
    raw = f.read().split("\n\n")

grid = raw[0].splitlines()
moves = raw[1].replace("\n", "")

# Step 1: Scale the map
room = []
for row in grid:
    new_row = []
    for ch in row:
        if ch == "#":
            new_row += ["#", "#"]
        elif ch == ".":
            new_row += [".", "."]
        elif ch == "O":
            new_row += ["[", "]"]
        elif ch == "@":
            new_row += ["@", "."]
    room.append(new_row)

ROWS, COLS = len(room), len(room[0])

# Step 2: Find robot
for r in range(ROWS):
    for c in range(COLS):
        if room[r][c] == "@":
            robot = (r, c)
            break

DIR = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


def move_horizontal(r, c, dc):
    nc = c + dc
    if room[r][nc] == ".":
        room[r][c], room[r][nc] = ".", "@"
        return (r, nc)

    if room[r][nc] not in "[]":
        return (r, c)

    boxes = []
    x = nc
    while room[r][x] in "[]":
        if room[r][x] == "[":
            boxes.append(x)
        x += dc

    if room[r][x] == "#":
        return (r, c)

    for b in reversed(boxes) if dc > 0 else boxes:
        room[r][b + dc] = "["
        room[r][b + dc + 1] = "]"
        room[r][b] = "."
        room[r][b + 1] = "."

    room[r][c], room[r][nc] = ".", "@"
    return (r, nc)


def move_vertical(r, c, dr):
    nr = r + dr
    if room[nr][c] == ".":
        room[r][c], room[nr][c] = ".", "@"
        return (nr, c)

    if room[nr][c] not in "[]":
        return (r, c)

    boxes = set()
    stack = [(nr, c if room[nr][c] == "[" else c - 1)]

    while stack:
        x, y = stack.pop()
        if (x, y) in boxes:
            continue
        boxes.add((x, y))

        nx = x + dr
        for ny in (y, y + 1):
            if room[nx][ny] == "[":
                stack.append((nx, ny))
            elif room[nx][ny] == "]":
                stack.append((nx, ny - 1))
            elif room[nx][ny] == "#":
                return (r, c)

    order = sorted(boxes, reverse=(dr > 0))
    for x, y in order:
        room[x + dr][y] = "["
        room[x + dr][y + 1] = "]"
        room[x][y] = "."
        room[x][y + 1] = "."

    room[r][c], room[nr][c] = ".", "@"
    return (nr, c)


# Step 3: Execute moves
for m in moves:
    dr, dc = DIR[m]
    r, c = robot
    if dr == 0:
        robot = move_horizontal(r, c, dc)
    else:
        robot = move_vertical(r, c, dr)

# Step 4: GPS calculation
ans = 0
for r in range(ROWS):
    for c in range(COLS):
        if room[r][c] == "[":
            ans += 100 * r + c

print(ans)

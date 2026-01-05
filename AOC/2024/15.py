room = []
moves = ''

with open('15.txt', 'r') as file:
    find_moves = False

    for line in file.readlines():
        line = line.strip()

        if line == '':
            find_moves = True
            continue

        if find_moves:
            moves += line
            continue

        room.append(list(line))

move_dir = {
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1),
    '^': (-1, 0)
}

ROWS = len(room)
COLS = len(room[0])
robot = None

for r in range(ROWS):
    if robot:
        break

    for c in range(COLS):
        if room[r][c] == '@':
            robot = (r, c)
            break

for move in moves:
    if move not in move_dir:
        continue

    x, y = move_dir[move]
    i, j = robot
    ix, jy = i + x, j + y

    if not (0 <= ix < ROWS and 0 <= jy < COLS):
        continue

    if room[ix][jy] == '#':
        continue

    if room[ix][jy] == '.':
        room[i][j] = '.'
        room[ix][jy] = '@'
        robot = (ix, jy)
        continue

    ixx, jyy = ix + x, jy + y

    while 0 <= ixx < ROWS and 0 <= jyy < COLS and room[ixx][jyy] == 'O':
        ixx += x
        jyy += y

    if 0 <= ixx < ROWS and 0 <= jyy < COLS and room[ixx][jyy] == '.':
        room[ixx][jyy] = 'O'
        room[ix][jy] = '@'
        room[i][j] = '.'
        robot = (ix, jy)


ans1 = 0

for r in range(ROWS):
    for c in range(COLS):
        if room[r][c] == 'O':
            ans1 += 100 * r + c

print(ans1)



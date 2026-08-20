from collections import deque

DIRS = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}


class Warehouse:
    def __init__(self, grid, part):
        self.room = self.expand(grid) if part == 2 else [list(row) for row in grid]
        self.rows = len(self.room)
        self.cols = len(self.room[0])
        self.robot = self.find_robot()
        self.part = part

    def expand(self, grid):
        room = []

        for row in grid:
            new_row = []

            for ch in row:
                if ch == "#":
                    new_row.extend("##")
                elif ch == ".":
                    new_row.extend("..")
                elif ch == "O":
                    new_row.extend("[]")
                elif ch == "@":
                    new_row.extend("@.")

            room.append(new_row)

        return room

    def find_robot(self):
        for r, row in enumerate(self.room):
            for c, ch in enumerate(row):
                if ch == "@":
                    return r, c

    def move(self, d):
        dr, dc = DIRS[d]
        r, c = self.robot

        if self.part == 1:
            self.move_part1(r, c, dr, dc)
        else:
            self.move_part2(r, c, dr, dc)

    def move_part1(self, r, c, dr, dc):
        nr, nc = r + dr, c + dc

        if self.room[nr][nc] == "#":
            return

        if self.room[nr][nc] == ".":
            self.room[r][c] = "."
            self.room[nr][nc] = "@"
            self.robot = (nr, nc)
            return

        x, y = nr, nc

        while self.room[x][y] == "O":
            x += dr
            y += dc

        if self.room[x][y] != ".":
            return

        self.room[x][y] = "O"
        self.room[nr][nc] = "@"
        self.room[r][c] = "."
        self.robot = (nr, nc)

    def move_part2(self, r, c, dr, dc):
        if dr == 0:
            self.move_horizontal(r, c, dc)
        else:
            self.move_vertical(r, c, dr)

    def move_horizontal(self, r, c, dc):
        nc = c + dc

        if self.room[r][nc] == "#":
            return

        if self.room[r][nc] == ".":
            self.room[r][c] = "."
            self.room[r][nc] = "@"
            self.robot = (r, nc)
            return

        cells = []
        x = nc

        while self.room[r][x] in "[]":
            cells.append(x)
            x += dc

        if self.room[r][x] == "#":
            return

        for pos in reversed(cells):
            self.room[r][pos + dc] = self.room[r][pos]

        self.room[r][c] = "."
        self.room[r][nc] = "@"
        self.robot = (r, nc)

    def move_vertical(self, r, c, dr):
        nr = r + dr

        if self.room[nr][c] == "#":
            return

        if self.room[nr][c] == ".":
            self.room[r][c] = "."
            self.room[nr][c] = "@"
            self.robot = (nr, c)
            return

        start_col = c if self.room[nr][c] == "[" else c - 1

        queue = deque([(nr, start_col)])
        boxes = set()

        while queue:
            x, y = queue.popleft()

            if (x, y) in boxes:
                continue

            boxes.add((x, y))

            nx = x + dr

            for ny in (y, y + 1):
                tile = self.room[nx][ny]

                if tile == "#":
                    return

                if tile == "[":
                    queue.append((nx, ny))

                elif tile == "]":
                    queue.append((nx, ny - 1))

        order = sorted(boxes, reverse=(dr > 0))

        for x, y in order:
            self.room[x][y] = "."
            self.room[x][y + 1] = "."

        for x, y in order:
            self.room[x + dr][y] = "["
            self.room[x + dr][y + 1] = "]"

        self.room[r][c] = "."
        self.room[nr][c] = "@"
        self.robot = (nr, c)

    def gps(self):
        total = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.part == 1 and self.room[r][c] == "O":
                    total += 100 * r + c

                if self.part == 2 and self.room[r][c] == "[":
                    total += 100 * r + c

        return total


def solve(part):
    with open("15.txt") as f:
        grid, moves = f.read().split("\n\n")

    grid = grid.splitlines()
    moves = moves.replace("\n", "")

    warehouse = Warehouse(grid, part)

    for move in moves:
        warehouse.move(move)

    return warehouse.gps()


print("Part 1:", solve(1))
print("Part 2:", solve(2))
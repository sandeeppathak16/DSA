def create_rectangle(rows, cols, grid):
    for r in range(rows):
        grid[r][:cols] = ['#'] * cols


def rotate_row(row, by, grid):
    by %= len(grid[row])
    grid[row] = grid[row][-by:] + grid[row][:-by]


def rotate_col(col, by, grid):
    by %= len(grid)

    column = [grid[r][col] for r in range(len(grid))]
    column = column[-by:] + column[:-by]

    for r, value in enumerate(column):
        grid[r][col] = value


def solve(filename="8.txt"):
    grid = [['.'] * 50 for _ in range(6)]

    with open(filename) as f:
        for operation in map(str.strip, f):

            if operation.startswith("rect"):
                cols, rows = map(
                    int,
                    operation.split()[1].split("x")
                )
                create_rectangle(rows, cols, grid)

            elif operation.startswith("rotate row"):
                row = int(operation.split("=")[1].split()[0])
                by = int(operation.split()[-1])
                rotate_row(row, by, grid)

            else:
                col = int(operation.split("=")[1].split()[0])
                by = int(operation.split()[-1])
                rotate_col(col, by, grid)

    lit_pixels = sum(cell == "#" for row in grid for cell in row)

    print("\n".join("".join(row) for row in grid))

    return lit_pixels
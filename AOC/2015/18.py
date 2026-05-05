def solve(filename='18.txt', part='1'):
    with open(filename) as f:
        lights = [list(line.strip()) for line in f]

    rows, cols = len(lights), len(lights[0])
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (-1, -1), (1, -1), (1, 1), (-1, 1)
    ]

    def force_corners_on(grid):
        grid[0][0] = grid[0][cols - 1] = '#'
        grid[rows - 1][0] = grid[rows - 1][cols - 1] = '#'

    def count_neighbors(r, c):
        return sum(
            1
            for dr, dc in directions
            if 0 <= r + dr < rows
            and 0 <= c + dc < cols
            and lights[r + dr][c + dc] == '#'
        )

    if part == '2':
        force_corners_on(lights)

    for _ in range(100):
        new_lights = [row[:] for row in lights]

        for r in range(rows):
            for c in range(cols):
                neighbors = count_neighbors(r, c)

                if lights[r][c] == '#':
                    new_lights[r][c] = '#' if neighbors in (2, 3) else '.'
                else:
                    new_lights[r][c] = '#' if neighbors == 3 else '.'

        if part == '2':
            force_corners_on(new_lights)

        lights = new_lights

    return sum(cell == '#' for row in lights for cell in row)
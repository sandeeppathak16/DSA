def solve(filename='1.txt'):
    with open(filename, 'r') as file:
        instructions = file.readline().strip().split(',')

    directions = ['N', 'E', 'S', 'W']

    moves = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }

    x, y = 0, 0
    direction_idx = 0

    visited = {(0, 0)}
    first_revisited = None

    for instruction in instructions:
        instruction = instruction.strip()

        turn = instruction[0]
        steps = int(instruction[1:])

        if turn == 'R':
            direction_idx = (direction_idx + 1) % 4
        else:
            direction_idx = (direction_idx - 1) % 4

        current_direction = directions[direction_idx]
        dx, dy = moves[current_direction]

        for _ in range(steps):
            x += dx
            y += dy

            if first_revisited is None and (x, y) in visited:
                first_revisited = (x, y)

            visited.add((x, y))

    final_distance = abs(x) + abs(y)

    revisited_distance = None
    if first_revisited:
        revisited_distance = (
            abs(first_revisited[0]) +
            abs(first_revisited[1])
        )

    return final_distance, revisited_distance
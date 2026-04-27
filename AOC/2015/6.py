import re

PATTERN = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')

def solve(part=1, filename='6.txt'):
    grid = [[0] * 1000 for _ in range(1000)]

    with open(filename) as file:
        for line in file:
            action, x1, y1, x2, y2 = PATTERN.search(line).groups()
            x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))

            for r in range(x1, x2 + 1):
                row = grid[r]
                for c in range(y1, y2 + 1):

                    if part == 1:
                        if action == 'turn on':
                            row[c] = 1
                        elif action == 'turn off':
                            row[c] = 0
                        else:
                            row[c] ^= 1

                    else:
                        if action == 'turn on':
                            row[c] += 1
                        elif action == 'turn off':
                            row[c] = max(0, row[c] - 1)
                        else:
                            row[c] += 2

    return sum(map(sum, grid))
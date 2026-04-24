def get_visited_houses(directions):
    x, y = 0, 0
    visited = {(x, y)}

    moves = {
        '^': (0, 1),
        'v': (0, -1),
        '>': (1, 0),
        '<': (-1, 0)
    }

    for d in directions:
        dx, dy = moves[d]
        x += dx
        y += dy
        visited.add((x, y))

    return visited


def solve1():
    with open('3.txt') as f:
        line = f.read().strip()

    return len(get_visited_houses(line))


def solve2():
    with open('3.txt') as f:
        line = f.read().strip()

    santa_moves = line[::2]   # even index
    robo_moves = line[1::2]   # odd index

    santa_visited = get_visited_houses(santa_moves)
    robo_visited = get_visited_houses(robo_moves)

    return len(santa_visited | robo_visited)


print(solve1(), solve2())
from collections import Counter


def solve(filename="2.txt"):
    with open(filename) as f:
        lines = f.readlines()

    direction = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }


    ans = ''

    pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pos = (1, 1)

    for line in lines:
        line = line.strip()

        for d in line:
            x1, y1 = direction[d]
            x, y = (pos[0] + x1), (pos[1] + y1)

            if 0 <= x < 3 and 0 <= y < 3:
                pos = (x, y)

        ans += str(pad[pos[0]][pos[1]])

    print(ans)


    pad = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, 'A', 'B', 'C', 0],
        [0, 0, 'D', 0, 0]
    ]

    ans = ''

    pos = (2, 0)

    for line in lines:
        line = line.strip()

        for d in line:
            x1, y1 = direction[d]
            x, y = (pos[0] + x1), (pos[1] + y1)

            if 0 <= x < 5 and 0 <= y < 5:
                if pad[x][y] != 0:
                    pos = (x, y)

        ans += str(pad[pos[0]][pos[1]])

    print(ans)


solve()
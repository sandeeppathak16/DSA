from collections import deque


def is_open(x, y, favorite_number):
    if x < 0 or y < 0:
        return False

    value = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    return bin(value).count("1") % 2 == 0


def solve(
    favorite_number=1362,
    start=(1, 1),
    target=(31, 39),
):
    q = deque([(start[0], start[1], 0)])
    visited = {start}

    part1 = None
    part2 = 0

    while q:
        x, y, steps = q.popleft()

        if steps <= 50:
            part2 += 1

        if (x, y) == target and part1 is None:
            part1 = steps
            
        if part1 is not None and steps > 50:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if (
                nx >= 0
                and ny >= 0
                and (nx, ny) not in visited
                and is_open(nx, ny, favorite_number)
            ):
                visited.add((nx, ny))
                q.append((nx, ny, steps + 1))

    return part1, part2


part1, part2 = solve()

print("Part 1:", part1)
print("Part 2:", part2)
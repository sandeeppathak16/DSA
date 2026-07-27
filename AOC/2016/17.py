from collections import deque
import hashlib

DIRECTIONS = [
    (-1, 0, "U"),
    (1, 0, "D"),
    (0, -1, "L"),
    (0, 1, "R"),
]

OPEN_DOORS = {"b", "c", "d", "e", "f"}


def solve(passcode: str, part_2: bool = False):
    queue = deque([(0, 0, "")])
    longest = 0

    while queue:
        row, col, path = queue.popleft()

        if (row, col) == (3, 3):
            if not part_2:
                return path

            longest = max(longest, len(path))
            continue

        digest = hashlib.md5((passcode + path).encode()).hexdigest()

        for ch, (dr, dc, move) in zip(digest[:4], DIRECTIONS):
            if ch not in OPEN_DOORS:
                continue

            nr, nc = row + dr, col + dc

            if 0 <= nr < 4 and 0 <= nc < 4:
                queue.append((nr, nc, path + move))

    return longest


print(solve("pslxynzg"))
print(solve("pslxynzg", True))
from math import prod


def read_grid(filename):
    with open(filename) as f:
        rows = [line.rstrip("\n") for line in f]

    if not rows:
        return []

    width = max(map(len, rows))
    return [row.ljust(width) for row in rows]


def solve(filename="6dec.txt", part=1):
    rows = read_grid(filename)

    if not rows:
        return 0

    problems = []

    if part == 1:
        op_row = rows[-1]
        number_rows = rows[:-1]
        width = len(rows[0])

        col = 0
        while col < width:

            while col < width and all(row[col] == " " for row in rows):
                col += 1

            if col == width:
                break

            start = col

            while col < width and not all(row[col] == " " for row in rows):
                col += 1

            end = col

            operator = next(
                (ch for ch in op_row[start:end] if ch != " "),
                None,
            )

            numbers = [
                int(chunk)
                for row in number_rows
                if (chunk := row[start:end].strip())
            ]

            problems.append((operator, numbers))

    elif part == 2:
        height = len(rows)
        width = len(rows[0])

        operator = None
        numbers = []

        for col in range(width):

            if all(rows[row][col] == " " for row in range(height)):
                if operator is not None or numbers:
                    problems.append((operator, numbers))

                operator = None
                numbers = []
                continue

            digits = []

            for row in range(height):
                ch = rows[row][col]

                if ch.isdigit():
                    digits.append(ch)
                elif ch in "+*":
                    operator = ch

            if digits:
                numbers.append(int("".join(digits)))

        if operator is not None or numbers:
            problems.append((operator, numbers))

    else:
        raise ValueError("part must be 1 or 2")

    answer = 0

    for operator, numbers in problems:
        if operator == "+":
            answer += sum(numbers)
        elif operator == "*":
            answer += prod(numbers)

    return answer


print(solve(part=1))
print(solve(part=2))
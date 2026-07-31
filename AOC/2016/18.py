TRAPS = {"..^", "^..", ".^^", "^^."}


def solve(row, rows=40):
    safe_tiles = row.count(".")

    for _ in range(rows - 1):
        next_row = []

        for i in range(len(row)):
            left = row[i - 1] if i > 0 else "."
            center = row[i]
            right = row[i + 1] if i < len(row) - 1 else "."

            pattern = left + center + right
            next_row.append("^" if pattern in TRAPS else ".")

        row = "".join(next_row)
        safe_tiles += row.count(".")

    return safe_tiles


row = "" \
"^.^^^..^^...^.^..^^^^^.....^" \
"...^^^..^^^^.^^.^^^^^^^^.^^.^" \
"^^^...^^...^^^^.^.^..^^..^..^." \
"^^.^.^......."

print(solve(row, rows=400000))
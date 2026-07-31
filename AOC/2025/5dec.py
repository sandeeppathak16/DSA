from bisect import bisect_right


def parse_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]

    split = lines.index("")

    ranges = [
        tuple(map(int, line.split("-")))
        for line in lines[:split]
    ]

    ids = [int(x) for x in lines[split + 1:]]

    return ranges, ids


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()

    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return [tuple(r) for r in merged]


def build_index(ranges):
    return [start for start, _ in ranges]


def in_range(value, ranges, starts):
    """Return True if value lies inside any range."""
    index = bisect_right(starts, value) - 1

    if index < 0:
        return False

    start, end = ranges[index]
    return start <= value <= end


def solve(filename="5dec.txt"):
    ranges, ids = parse_input(filename)

    merged = merge_ranges(ranges)
    starts = build_index(merged)

    # Part 1
    part1 = sum(
        in_range(value, merged, starts)
        for value in ids
    )

    # Part 2
    part2 = sum(
        end - start + 1
        for start, end in merged
    )

    return part1, part2


print(solve())
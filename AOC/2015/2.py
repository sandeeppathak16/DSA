def part1(filename='2.txt'):
    with open(filename, 'r') as file:
        inputs = [list(map(int, line.strip().split('x'))) for line in file]

    ans = 0
    for l, w, h in inputs:
        side1 = l * w
        side2 = w * h
        side3 = h * l

        ans += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

    return ans


def part2(filename='2.txt'):
    import math

    ans = 0
    with open(filename, 'r') as file:
        for line in file:
            l, w, h = map(int, line.strip().split('x'))

            dims = sorted([l, w, h])  # safest way
            min1, min2, max1 = dims

            ribbon = 2 * (min1 + min2)
            bow = math.prod(dims)

            ans += ribbon + bow

    return ans


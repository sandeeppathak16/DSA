def rotate_left(chars, steps):
    steps %= len(chars)
    return chars[steps:] + chars[:steps]


def rotate_right(chars, steps):
    steps %= len(chars)
    return chars[-steps:] + chars[:-steps]


def solve(filename="21.txt", password="abcdefgh", un_scrambled=False):
    with open(filename) as f:
        operations = [line.split() for line in f]

    if un_scrambled:
        operations.reverse()

    chars = list(password)

    for op in operations:
        command = op[0]

        if command == "swap":
            if op[1] == "position":
                x, y = int(op[2]), int(op[5])
            else:
                x, y = chars.index(op[2]), chars.index(op[5])

            chars[x], chars[y] = chars[y], chars[x]

        elif command == "rotate":
            direction = op[1]

            if direction == "left":
                rotate = rotate_right if un_scrambled else rotate_left
                chars = rotate(chars, int(op[2]))

            elif direction == "right":
                rotate = rotate_left if un_scrambled else rotate_right
                chars = rotate(chars, int(op[2]))

            else:
                letter = op[6]

                if un_scrambled:
                    for steps in range(len(chars)):
                        candidate = rotate_left(chars, steps)

                        idx = candidate.index(letter)
                        rotations = 1 + idx + (idx >= 4)

                        if rotate_right(candidate, rotations) == chars:
                            chars = candidate
                            break
                else:
                    idx = chars.index(letter)
                    rotations = 1 + idx + (idx >= 4)
                    chars = rotate_right(chars, rotations)

        elif command == "reverse":
            start, end = int(op[2]), int(op[4])
            chars[start : end + 1] = reversed(chars[start : end + 1])

        else:  # move
            src = int(op[5]) if un_scrambled else int(op[2])
            dst = int(op[2]) if un_scrambled else int(op[5])

            chars.insert(dst, chars.pop(src))

    return "".join(chars)


print(solve())
print(solve(password="fbgdceah", un_scrambled=True))
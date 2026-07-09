def decompressed_length(s, recursive=False):
    total = 0
    i = 0

    while i < len(s):
        if s[i] != '(':
            total += 1
            i += 1
        else:
            j = i

            while s[j] != ')':
                j += 1

            chars, repeat = map(int, s[i + 1:j].split('x'))

            if recursive:
                segment = s[j + 1:j + 1 + chars]
                total += decompressed_length(segment, True) * repeat
            else:
                total += chars * repeat

            i = j + 1 + chars

    return total


def solve(filename='9.txt', part2=False):
    with open(filename) as f:
        line = f.readline().strip()

    return decompressed_length(line, recursive=part2)
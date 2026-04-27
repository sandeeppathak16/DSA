def solve(inputs):
    code = 0
    memory = 0

    for codes in inputs:
        code += len(codes)

        i = 1
        while i < len(codes) - 1:
            ch = codes[i]

            if ch != '\\':
                memory += 1
                i += 1

            elif ch == '\\' and codes[i + 1] in {'\\', '"'}:
                memory += 1
                i += 2

            elif ch == '\\' and codes[i + 1] == 'x':
                memory += 1
                i += 4

    return code - memory


def solve1():
    with open('8.txt', 'r') as file:
        inputs = [line.strip() for line in file.readlines()]

    return solve(inputs)


def solve2():
    with open('8.txt', 'r') as file:
        inputs = []

        for line in file.readlines():
            line = line.strip()

            new_line = '"'
            for ch in line:
                if ch == '"' or ch == '\\':
                    new_line += '\\' + ch
                else:
                    new_line += ch
            new_line += '"'

            inputs.append(new_line)

    return solve(inputs)
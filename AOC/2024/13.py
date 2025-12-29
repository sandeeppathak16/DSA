import re

with open('13.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

    problems = []
    i = 0
    while i < len(lines):
        j = i
        while j < len(lines):
            if lines[j] == '':
                break

            j += 1

        problems.append(lines[i:j])
        i = j + 1


def solve(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1

    if det == 0:
        return 0

    a = (c1 * b2 - c2 * b1) / det
    b = (a1 * c2 - a2 * c1) / det

    # print(a, b, a.is_integer(), b.is_integer())
    if a.is_integer() and b.is_integer():
        return int(a), int(b)

    return 0, 0


def extract_xy(text):
    return [int(v) for _, v in re.findall(r'([XY])\s*[+=]\s*(\d+)', text)]


ans1 = 0
for problem in problems:
    a1, a2 = extract_xy(problem[0])
    b1, b2 = extract_xy(problem[1])
    c1, c2 = extract_xy(problem[2])

    # print(a1, b1, c1, a2, b2, c2)
    a, b = solve(a1, b1, c1 + 10000000000000, a2, b2, c2 + 10000000000000)
    ans1 += ((a * 3) + b)

print(ans1)

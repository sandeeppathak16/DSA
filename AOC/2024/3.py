import re

lines = []

with open('3.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip())


ans1 = 0
for line in lines:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)
    for x, y in matches:
        ans1 += (int(x) * int(y))

print(ans1)

ans2 = 0
disabled = False

for line in lines:
    i = 0

    while i < len(line):

        if line[i:i+7] == "don't()":
            disabled = True
            i += 7
            continue

        if line[i:i+4] == "do()":
            disabled = False
            i += 4
            continue

        if not disabled and line[i:i+4] == "mul(":
            start = i + 4
            j = start

            while j < len(line) and line[j] != ')':
                if not (line[j].isdigit() or line[j] == ','):
                    break
                j += 1

            if j < len(line) and line[j] == ')':
                payload = line[start:j]
                parts = payload.split(',')

                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    ans2 += int(parts[0]) * int(parts[1])
                    i = j + 1
                    continue

            i = start
            continue

        i += 1

print(ans2)







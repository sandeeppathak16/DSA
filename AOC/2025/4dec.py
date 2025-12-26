import collections

with open('4dec.txt', 'r') as file:
    codes = [list(line.strip()) for line in file if line.strip()]


direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

row = len(codes)
col = len(codes[0])

ans = 0

for _ in range(row):
    change = collections.defaultdict(list)
    for i in range(row):
        for j in range(col):
            if codes[i][j] == '@':
                count = 0
                for dr, dc in direction:
                    nr, nc = i + dr, j + dc

                    if 0 <= nr <= row and 0 <= nc < col and codes[nr][nc] == '@':
                        count += 1

                if count < 4:
                    change[i].append(j)
                    ans += 1

    for i in change:
        for j in change[i]:
            codes[i][j] = 'x'



print(ans)
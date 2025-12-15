from functools import lru_cache

with open("7dec.txt", "r") as f:
    codes = [list(line.strip()) for line in f.readlines()]

s_index = codes[0].index('S')

checks = [s_index]
ans = 0


for code in codes[1:]:
    new_checks = set()
    for check in checks:
        if code[check] == '.':
            new_checks.add(check)
        elif code[check] == '^':
            ans += 1
            new_beam1, new_beam2 = check + 1, check - 1
            if new_beam1 < len(code):
                new_checks.add(new_beam1)
            if new_beam2 >= 0:
                new_checks.add(new_beam2)

    checks = list(new_checks)

print(ans)

rows = len(codes)
cols = len(codes[0])


@lru_cache(maxsize=None)
def ways(r, c):
    if c < 0 or c >= cols:
        return 1
    if r >= rows:
        return 1

    ch = codes[r][c]
    if ch == '^':
        return ways(r + 1, c - 1) + ways(r + 1, c + 1)
    else:
        return ways(r + 1, c)


result = ways(0, s_index)
print(result)

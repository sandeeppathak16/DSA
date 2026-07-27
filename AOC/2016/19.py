def solve(n):

    mapping = {i: 1 for i in range(n)}
    start = 0

    while True:
        if mapping[start % n] == 0:
            start += 1
            continue

        mapping[start] = mapping[(start + 1) % n]
        if mapping[(start + 1) % n] > 0:
            mapping[(start + 1) % n] -= 1

        if mapping[start] == n:
            return start
        else:
            start = (start + 1) % n


print(solve(5))

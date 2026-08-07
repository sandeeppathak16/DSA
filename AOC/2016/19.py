def solve(n, part=1):
    if part == 1:
        p = 1
        while p * 2 <= n:
            p *= 2

        return 2 * (n - p) + 1

    elif part == 2:
        p = 1
        while p * 3 <= n:
            p *= 3

        if n == p:
            return n
        elif n <= 2 * p:
            return n - p
        else:
            return 2 * n - 3 * p
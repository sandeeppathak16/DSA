def solve(filename="3.txt"):
    with open(filename) as f:
        lines = f.readlines()

    # Part 1

    triangles = []

    for line in lines:
        line = line.strip()
        triangles.append(list(map(int, line.split())))

    ans = 0

    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            ans += 1

    print(ans)

    # Part 2

    ans = 0

    def get_triangle(triangle):
        start = 0
        end = 3

        while end < len(triangle):
            yield triangle[start:end]
            start = end
            end += 3

        yield triangle[start:end]

    for triangle in get_triangle(triangles):
        for a, b, c in zip(triangle[0], triangle[1], triangle[2]):
            if a + b > c and a + c > b and b + c > a:
                ans += 1

    print(ans)


solve()
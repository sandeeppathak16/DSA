import math

coords = []
with open("8dec.txt") as f:
    for line in f:
        x, y, z = map(int, line.split(","))
        coords.append((x, y, z))

n = len(coords)

edges = []
for i in range(n):
    x1, y1, z1 = coords[i]
    for j in range(i + 1, n):
        x2, y2, z2 = coords[j]
        d = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
        edges.append((d, i, j))

edges.sort()

parent = list(range(n))
size = [1] * n


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True


components = n
last_edge = None
for d, i, j in edges:
    if union(i, j):
        components -= 1
        last_edge = (i, j)
        if components == 1:
            break

i, j = last_edge
answer = coords[i][0] * coords[j][0]
print(answer)

# components = {}
# for node in range(n):
#     root = find(node)
#     components[root] = components.get(root, 0) + 1
#
# sizes = sorted(components.values(), reverse=True)
# print("Component sizes:", sizes)
# ans = sizes[0] * sizes[1] * sizes[2]
# print("Answer:", ans)

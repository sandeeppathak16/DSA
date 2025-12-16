
ids = []
with open('1.txt', 'r') as f:
    for line in f.readlines():
        id = [int(i) for i in line.strip().split(' ') if i]
        ids.append(id)

ids1 = []
ids2 = []

for i, j in ids:
    ids1.append(i)
    ids2.append(j)

ids1.sort()
ids2.sort()

ans1 = 0
for i, j in zip(ids1, ids2):
    # print(i, j)
    ans1 += abs(j - i)

print(ans1)

ans2 = 0

for num in ids1:
    ans2 += (num * (ids2.count(num)))

print(ans2)

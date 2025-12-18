import collections

ordering_rules = collections.defaultdict(list)
found_updates = False
updates = []
with open('5.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        if line == '':
            found_updates = True

        if found_updates and line:
            updates.append(line.split(','))
        else:
            if not line:
                continue

            x, y = line.split('|')
            ordering_rules[x].append(y)

ans1 = 0
ans2 = 0

for update in updates:
    pos = {page: i for i, page in enumerate(update)}
    valid = True

    for x in update:
        for y in ordering_rules.get(x, []):
            if y in pos and pos[y] < pos[x]:
                valid = False
                break
        if not valid:
            break

    if valid:
        ans1 += int(update[len(update)//2])
        continue

    graph = collections.defaultdict(list)
    indegree = {p: 0 for p in update}

    for x in update:
        for y in ordering_rules.get(x, []):
            if y in indegree:
                graph[x].append(y)
                indegree[y] += 1

    q = collections.deque([p for p in indegree if indegree[p] == 0])
    ordered = []

    while q:
        node = q.popleft()
        ordered.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    mid = len(ordered) // 2
    ans2 += int(ordered[mid])

print(ans1, ans2)







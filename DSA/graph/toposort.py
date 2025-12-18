from collections import deque


def dfs(graph):
    n = len(graph)
    stack = []
    state = [0] * n
    has_cycle = False

    def helper(node):
        nonlocal has_cycle

        if state[node] == 1:
            has_cycle = True
            return

        if state[node] == 2:
            return

        state[node] = 1

        for nei, connected in enumerate(graph[node]):
            if connected:
                helper(node)

        state[node] = 2
        stack.append(node)

    for node in range(n):
        if not state[node]:
            helper(node)

    if has_cycle:
        raise Exception('cyclic graph')

    return stack[::-1]


def bfs(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for nei in graph[node]:
            indegree[nei] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    stack = []
    count = 0
    while queue:
        node = queue.popleft()
        stack.append(node)
        count += 1

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)

    if count != len(graph):
        raise Exception('cyclic graph')

    return stack


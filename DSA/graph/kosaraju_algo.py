import collections


def kosaraju_algo(n, connections):
    graph = collections.defaultdict(list)
    reversed_graph = collections.defaultdict(list)

    for u, v in connections:
        graph[u].append(v)
        reversed_graph[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    res = []

    def dfs2(u, sub_res):
        visited[u] = True
        sub_res.append(u)
        for v in reversed_graph[u]:
            if not visited[v]:
                dfs2(v, sub_res)

    for node in reversed(order):
        if not visited[node]:
            sub_res = []
            dfs2(node, sub_res)
            res.append(sub_res)

    return res

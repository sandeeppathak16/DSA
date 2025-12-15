import collections


def articulation_points(n, connections):
    graph = collections.defaultdict(list)

    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    is_ap = [False] * n
    visited = [False] * n
    time = 0

    def dfs(u):
        global time
        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1

        c = 0
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)

                low[u] = min(low[u], low[v])

                if parent[u] == -1 and c > 1:
                    is_ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    is_ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

        for node in range(n):
            if not visited[node]:
                dfs(node)

        return [node for node in range(n) if is_ap[node]]


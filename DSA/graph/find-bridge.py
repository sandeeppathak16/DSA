import collections


def find_bridge(n, edge):
    graph = collections.defaultdict(set)

    for u, v in edge:
        graph[u].add(v)
        graph[v].add(u)

    def bridge(u, visisted, parent, low, disc, time):
        visisted[u] = True

        low[u] = time[0]
        disc[u] = time[0]
        time[0] += 1

        ans = []

        for v in graph[u]:
            if not visisted[v]:
                parent[v] = u
                find = bridge(v, visisted, parent, low, disc, time)
                ans.extend(find)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    ans.append([u, v])

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

        return ans

    visited = [False] * n
    disc = [float('inf')] * n
    low = [float('inf')] * n
    parent = [-1] * n
    time = [0]

    ans = []

    for node in range(n):
        if not visited[node]:
            ans.extend(bridge(u, visited, parent=parent, disc=disc, low=low, time=time))

    return ans

from functools import lru_cache

graph = {}
with open("11dec.txt") as f:
    for line in f:
        line = line.strip()
        u, v = line.split(':')
        v = v.strip().split(' ')
        graph[u] = v


def count_paths(node, graph, memo):
    if node == 'out':
        return 1

    if node in memo:
        return memo[node]

    total = 0
    for nei in graph.get(node, []):
        total += count_paths(nei, graph, memo)

    memo[node] = total
    return total


memo = {}
ans = count_paths('you', graph, memo)
print("Total paths:", ans)


def count_paths_seen(node, fft_seen, dac_seen):
    if node == 'fft':
        fft_seen = True
    if node == 'dac':
        dac_seen = True

    if node == 'out':
        return 1 if fft_seen and dac_seen else 0

    total = 0
    for nei in graph.get(node, []):
        total += count_paths(nei, fft_seen, dac_seen)

    return total


count_paths = lru_cache(None)(count_paths)
ans = count_paths('svr', False, False)
print("Total paths:", ans)

import itertools
import re


def solve(filename='9.txt'):

    pattern = r'^(\w+)\s+to\s+(\w+)\s+=\s+(\d+)$'

    graph = {}
    nodes = set()

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(pattern, line.strip())
            if match:
                a, b, d = match.groups()
                d = int(d)

                graph[(a, b)] = d
                graph[(b, a)] = d

                nodes.add(a)
                nodes.add(b)

    ans_part1 = float('inf')
    ans_part2 = float('-inf')

    for perm in itertools.permutations(nodes):
        cost = 0
        pruned = False

        for i in range(len(perm) - 1):
            cost += graph[(perm[i], perm[i + 1])]

            if cost >= ans_part1:
                pruned = True

        if not pruned:
            ans_part1 = min(ans_part1, cost)

        ans_part2 = max(ans_part2, cost)

    return ans_part1, ans_part2
from itertools import combinations
from math import prod


def can_partition(packages, groups, target):
    if groups == 1:
        return sum(packages) == target

    n = len(packages)

    for r in range(1, n + 1):
        for comb in combinations(packages, r):
            if sum(comb) == target:
                remaining = list(packages)

                for x in comb:
                    remaining.remove(x)

                if can_partition(remaining, groups - 1, target):
                    return True

    return False


def solve(filename="24.txt", groups=3):
    with open(filename) as file:
        packages = [int(line.strip()) for line in file]

    total = sum(packages)

    target = total // groups

    packages.sort(reverse=True)

    best_qe = float("inf")
    best_len = float("inf")

    n = len(packages)

    for size in range(1, n + 1):

        found = False

        for comb in combinations(packages, size):

            if sum(comb) != target:
                continue

            remaining = list(packages)

            for x in comb:
                remaining.remove(x)

            if not can_partition(remaining, groups - 1, target):
                continue

            qe = prod(comb)

            if qe < best_qe:
                best_qe = qe
                best_len = size

            found = True

        if found:
            break

    return best_qe
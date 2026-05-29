from collections import Counter

def solve(filename='6.txt', part1=True):
    with open(filename) as f:
        words = [line.strip() for line in f]

    result = []

    for column in zip(*words):
        counts = Counter(column)

        if part1:
            result.append(max(counts, key=counts.get))
        else:
            result.append(min(counts, key=counts.get))

    return ''.join(result)

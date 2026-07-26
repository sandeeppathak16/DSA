def frequencySort(s: str) -> str:
    from collections import Counter

    counter = Counter(s)
    n = len(s)

    bucket = [[] for _ in range(n + 1)]

    for ch, count in counter.items():
        bucket[count].append(ch * count)

    return "".join("".join(bucket[i]) for i in range(n, 0, -1))
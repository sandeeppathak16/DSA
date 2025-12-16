nums = []
with open('2.txt', 'r') as f:
    for line in f:
        nums.append(list(map(int, line.split())))


def is_safe(report):
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]

    if any(d == 0 or abs(d) > 3 for d in diffs):
        return False

    return all(d > 0 for d in diffs) or all(d < 0 for d in diffs)

ans1 = 0
ans2 = 0

for num in nums:
    if is_safe(num):
        ans2 += 1
        ans1 += 1
        continue

    for i in range(len(num)):
        if is_safe(num[:i] + num[i + 1:]):
            ans2 += 1
            break

print(ans1, ans2)


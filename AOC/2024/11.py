from collections import defaultdict

with open("11.txt") as f:
    numbers = list(map(int, f.read().strip().split()))


for _ in range(75):
    new_numbers = []
    for ele in numbers:
        if ele == 0:
            new_numbers.append(1)

        elif len(str(ele)) % 2 == 0:
            str_ele = str(ele)
            new_numbers.extend([int(str_ele[:len(str_ele)//2]), int(str_ele[len(str_ele)//2:])])
        else:
            new_numbers.append(ele * 2024)

    numbers = new_numbers

print(len(numbers))


counts = defaultdict(int)
for n in numbers:
    counts[n] += 1

for _ in range(75):
    new_counts = defaultdict(int)

    for num, cnt in counts.items():
        if num == 0:
            new_counts[1] += cnt

        else:
            s = str(num)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left = int(s[:mid])
                right = int(s[mid:])
                new_counts[left] += cnt
                new_counts[right] += cnt
            else:
                new_counts[num * 2024] += cnt

    counts = new_counts

print(sum(counts.values()))

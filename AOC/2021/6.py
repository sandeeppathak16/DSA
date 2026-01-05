from collections import Counter

with open('6.txt', 'r') as f:
    lanternfish = list(map(int, f.readline().strip().split(',')))


counter = Counter(lanternfish)

for _ in range(256):
    new_counter = Counter()

    for fish, count in counter.items():
        if fish == 0:
            new_counter[6] += count
            new_counter[8] += count
        else:
            new_counter[fish - 1] += count

    counter = new_counter

print(sum(counter.values()))


for _ in range(80):
    new_lanternfish = []
    existing_lanternfish = []

    for fish in lanternfish:
        if fish == 0:
            new_lanternfish.append(8)
            fish = 6
        else:
            fish -= 1

        existing_lanternfish.append(fish)

    lanternfish = existing_lanternfish + new_lanternfish

print(len(lanternfish))

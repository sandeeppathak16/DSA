import collections
from itertools import product

_input = collections.defaultdict(list)

with open('7.txt', 'r') as f:
    for line in f.readlines():
        key, numbers = line.strip().split(':', maxsplit=1)
        _input[key] = list(map(int, numbers.strip().split(' ')))


ans = 0
second = True
items = ['+', '*'] + (['||'] if second else [])

for key, value in _input.items():
    gaps = len(value) - 1
    for arrangement in product(items, repeat=gaps):
        all_value = value[0]
        i = 1
        for op in arrangement:
            if op == '+':
                all_value += value[i]
            elif op == '||':
                all_value = int(str(all_value) + str(value[i]))
            else:
                all_value *= value[i]

            i += 1

        if all_value == int(key):
            ans += int(key)
            break

print(ans)




import re
from itertools import permutations

PATTERN = r'^(\w+)\s+would\s+(gain|lose)\s+(\d+)\s+happiness units by sitting next to\s+(\w+)\.'

def solve(filename='13.txt', part_2=False):
    mapping = {}
    attendees = set()

    with open(filename, 'r') as file:
        for line in file:
            match = re.match(PATTERN, line)

            if match:
                p1, action, amt, p2 = match.groups()
                amt = int(amt) * (1 if action == "gain" else -1)

                mapping[(p1, p2)] = amt
                attendees.update([p1, p2])

    if part_2:
        for attendee in attendees:
            mapping[('me', attendee)] = 0
            mapping[(attendee, 'me')] = 0

        attendees.add('me')

    ans = float('-inf')

    for arrangement in permutations(attendees):
        current_total = 0
        n = len(arrangement)

        for i in range(n):
            j = (i + 1) % n

            a = arrangement[i]
            b = arrangement[j]

            current_total += mapping[(a, b)]
            current_total += mapping[(b, a)]

        ans = max(ans, current_total)

    return ans
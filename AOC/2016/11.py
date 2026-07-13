from collections import deque
from itertools import combinations


def is_safe(floor):
    generators = {item for item in floor if item.endswith("G")}

    if not generators:
        return True

    for item in floor:
        if item.endswith("M") and item[:-1] + "G" not in generators:
            return False

    return True


def goal(floors):
    return all(len(floors[i]) == 0 for i in range(3))


def add_state(queue, state, elevator, new_floor, remaining, moved_items, step):
    destination = state[new_floor].copy()
    destination.extend(moved_items)

    if not (is_safe(remaining) and is_safe(destination)):
        return

    new_state = [floor.copy() for floor in state]
    new_state[elevator] = remaining
    new_state[new_floor] = destination

    queue.append((step + 1, new_state, new_floor))


def solve(floors):
    queue = deque([(0, floors, 0)])
    visited = set()

    while queue:
        step, state, elevator = queue.popleft()

        if goal(state):
            return step

        key = (
            elevator,
            tuple(tuple(sorted(floor)) for floor in state),
        )

        if key in visited:
            continue

        visited.add(key)

        for item in state[elevator]:
            remaining = state[elevator].copy()
            remaining.remove(item)

            if elevator > 0:
                add_state(queue, state, elevator, elevator - 1, remaining, [item], step)

            if elevator < 3:
                add_state(queue, state, elevator, elevator + 1, remaining, [item], step)


        for item1, item2 in combinations(state[elevator], 2):
            remaining = state[elevator].copy()
            remaining.remove(item1)
            remaining.remove(item2)

            if elevator > 0:
                add_state(queue, state, elevator, elevator - 1, remaining, [item1, item2], step)

            if elevator < 3:
                add_state(queue, state, elevator, elevator + 1, remaining, [item1, item2], step)


part_1_floors = [
    ["PG", "PM"],
    ["CG", "UG", "RG", "LG"],
    ["CM", "UM", "RM", "LM"],
    [],
]


part_2_floors = [
    ["PG", "PM", "EG", "EM", "DG", "DM"],
    ["CG", "UG", "RG", "LG"],
    ["CM", "UM", "RM", "LM"],
    [],
]
print(solve(floors=part_2_floors))
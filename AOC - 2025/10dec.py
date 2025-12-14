import pulp
import heapq
from itertools import combinations
from collections import deque


machines = []

with open("10dec.txt") as f:
    for line in f:
        line = line.strip()

        start_sq = line.index('[')
        end_sq = line.index(']')
        pattern = line[start_sq + 1:end_sq]
        target = [1 if c == '#' else 0 for c in pattern]

        start_btn = end_sq + 1
        start_curly = line.index('{')
        button_part = line[start_btn:start_curly].strip()
        end_curly = line.index('}')

        buttons = []
        i = 0
        while i < len(button_part):
            if button_part[i] == '(':
                j = i + 1
                while button_part[j] != ')':
                    j += 1
                button = list(map(int, button_part[i+1:j].split(',')))
                buttons.append(button)
                i = j
            i += 1

        target_2 = list(map(int, line[start_curly + 1:end_curly].split(',')))

        machines.append({
            "target": target,
            "target_2": target_2,
            "buttons": buttons
        })


def min_presses_joltage(target, buttons):
    n = len(target)
    start = tuple([0] * n)
    target = tuple(target)

    q = deque()
    q.append((start, 0))
    visited = set()
    visited.add(start)

    while q:
        state, steps = q.popleft()

        if state == target:
            return steps

        for btn in buttons:
            new_state = list(state)
            valid = True

            for idx in btn:
                new_state[idx] += 1
                if new_state[idx] > target[idx]:
                    valid = False
                    break

            if not valid:
                continue

            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, steps + 1))

    return float('inf')


def min_presses_joltage_fast(target, buttons):
    n = len(target)
    target = tuple(target)
    start = tuple([0] * n)

    def heuristic(state):
        # minimum remaining presses needed
        return max(target[i] - state[i] for i in range(n))

    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start))

    visited = {start: 0}

    while pq:
        _, cost, state = heapq.heappop(pq)

        if state == target:
            return cost

        for btn in buttons:
            new_state = list(state)
            valid = True

            for idx in btn:
                new_state[idx] += 1
                if new_state[idx] > target[idx]:
                    valid = False
                    break

            if not valid:
                continue

            new_state = tuple(new_state)
            new_cost = cost + 1

            if new_state not in visited or new_cost < visited[new_state]:
                visited[new_state] = new_cost
                priority = new_cost + heuristic(new_state)
                heapq.heappush(pq, (priority, new_cost, new_state))

    return float('inf')


def min_presses_ilp(target, buttons):
    """
    target: list[int]
    buttons: list[list[int]]
    """

    num_buttons = len(buttons)
    num_counters = len(target)

    # Create problem
    prob = pulp.LpProblem("Joltage_Min_Presses", pulp.LpMinimize)

    # Variables: how many times each button is pressed
    x = [
        pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer")
        for i in range(num_buttons)
    ]

    # Objective: minimize total presses
    prob += pulp.lpSum(x)

    # Constraints: each counter must reach target exactly
    for j in range(num_counters):
        prob += (
            pulp.lpSum(x[i] for i in range(num_buttons) if j in buttons[i])
            == target[j]
        )

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    return int(pulp.value(prob.objective))


ans = 0
for idx, m in enumerate(machines, 1):
    button = m["buttons"]
    target = m["target"]
    target_2 = m["target_2"]
    presses = min_presses_ilp(target_2, button)
    if presses != float('inf'):
        ans += presses

    # solution for first problem
    button_i = list(range(len(button)))

    all_combos = []
    for r in range(1, len(button_i) + 1):
        all_combos.extend(combinations(button_i, r))

    for comb in all_combos:
        start = [0] * len(target)
        for i in comb:
            for b in button[i]:
                start[b] = 1 if start[b] == 0 else 0

        if start == target:
            ans += len(comb)
            break

print(ans)


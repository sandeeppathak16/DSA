import re

PATTERN = re.compile(r'^(?:(NOT)\s+)?(\w+)(?:\s+(AND|OR|LSHIFT|RSHIFT)\s+(\w+))?\s*->\s*(\w+)$')

def solve(filename='7.txt'):
    inputs = []

    with open(filename) as file:
        for line in file:
            match = PATTERN.match(line.strip())
            if match:
                inputs.append(match.groups())

    mp = {}
    
    for unary_op, left, op, right, target in inputs:
        mp[target] = [unary_op, left, op, right]

    cache = {}

    operator_mapping = {
        'OR': lambda a, b: a | b,
        'AND': lambda a, b: a & b,
        'RSHIFT': lambda a, b: a >> b,
        'LSHIFT': lambda a, b: a << b
    }

    def get_value(x):
        if x.isdigit():
            return int(x)
        if x in cache:
            return cache[x]
        return solve_gate(x)

    def solve_gate(target):
        if target in cache:
            return cache[target]

        unary_op, left, op, right = mp[target]

        if not unary_op and not op:
            val = get_value(left)

        elif unary_op:
            val = ~get_value(left) & 0xFFFF

        else:
            left_val = get_value(left)
            right_val = get_value(right)
            val = operator_mapping[op](left_val, right_val)

        cache[target] = val & 0xFFFF
        return cache[target]

    part_1_ans = solve_gate('a')
    cache = {'b': part_1_ans}
    part_2_ans = solve_gate('a')

    return part_1_ans, part_2_ans
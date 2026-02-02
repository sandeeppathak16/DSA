# | Opcode | Name | Effect                             |
# | ------ | ---- | ---------------------------------- |
# | 0      | adv  | Divide A by 2^combo → store in A   |
# | 1      | bxl  | B = B XOR literal                  |
# | 2      | bst  | B = (combo % 8)                    |
# | 3      | jnz  | If A ≠ 0, jump instruction pointer |
# | 4      | bxc  | B = B XOR C                        |
# | 5      | out  | Output (combo % 8)                 |
# | 6      | bdv  | Divide A by 2^combo → store in B   |
# | 7      | cdv  | Divide A by 2^combo → store in C   |

# | Operand | Meaning                |
# | ------- | ---------------------- |
# | 0–3     | Literal values 0–3     |
# | 4       | Value of register A    |
# | 5       | Value of register B    |
# | 6       | Value of register C    |
# | 7       | Invalid (won’t appear) |


import re
from collections import deque

with open("17.txt") as f:
    lines = f.readlines()

register = {
    'a': 0,
    'b': 0,
    'c': 0,
}

key = 'a'
program = []
program_started = False

for line in lines:
    line = line.strip()

    if not line:
        program_started = True
        continue

    if not program_started:
        register[key] = int(re.findall(r"\d+", line)[0])
        key = chr(ord(key) + 1)
    else:
        program.extend(list(map(int, re.findall(r"-?\d+", line))))


def run_vm(program, A):
    reg = {'a': A, 'b': 0, 'c': 0}
    ip = 0
    output = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if operand <= 3:
            combo = operand
        elif operand == 4:
            combo = reg['a']
        elif operand == 5:
            combo = reg['b']
        elif operand == 6:
            combo = reg['c']
        else:
            raise ValueError("Invalid operand")

        jumped = False

        if opcode == 0:      # adv
            reg['a'] //= (2 ** combo)
        elif opcode == 1:    # bxl
            reg['b'] ^= operand
        elif opcode == 2:    # bst
            reg['b'] = combo % 8
        elif opcode == 3:    # jnz
            if reg['a'] != 0:
                ip = operand
                jumped = True
        elif opcode == 4:    # bxc
            reg['b'] ^= reg['c']
        elif opcode == 5:    # out
            output.append(combo % 8)
        elif opcode == 6:    # bdv
            reg['b'] = reg['a'] // (2 ** combo)
        elif opcode == 7:    # cdv
            reg['c'] = reg['a'] // (2 ** combo)

        if not jumped:
            ip += 2

    return output

def find_minimum_A(program):
    target = program
    queue = deque()

    # start with smallest positive A digits
    for d in range(1, 8):
        queue.append(d)

    while queue:
        a = queue.popleft()
        out = run_vm(program, a)

        # prune: output must match program prefix
        if out != target[:len(out)]:
            continue

        # success
        if out == target:
            return a

        # expand search (append base-8 digit)
        for d in range(8):
            queue.append((a << 3) | d)

    raise RuntimeError("No solution found")



# program = [2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0]
answer = find_minimum_A(program)
print(answer)

def solve(filename='23.txt', a=0):
    instructions = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().replace(',', '').split()

            if parts[0] == 'jmp':
                instructions.append((parts[0], '', parts[1]))
            elif parts[0] in ('jie', 'jio'):
                instructions.append((parts[0], parts[1], parts[2]))
            else:
                instructions.append((parts[0], parts[1], ''))

    registers = {
        'a': a,
        'b': 0
    }

    pointer = 0

    while 0 <= pointer < len(instructions):
        instruction, register, move = instructions[pointer]

        if instruction == 'hlf':
            registers[register] //= 2
            pointer += 1

        elif instruction == 'tpl':
            registers[register] *= 3
            pointer += 1

        elif instruction == 'inc':
            registers[register] += 1
            pointer += 1

        elif instruction == 'jmp':
            pointer += int(move)

        elif instruction == 'jie':
            pointer += int(move) if registers[register] % 2 == 0 else 1

        elif instruction == 'jio':
            pointer += int(move) if registers[register] == 1 else 1

    return registers


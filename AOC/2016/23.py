def solve(filename="23.txt", initial=None):
    if initial is None:
        initial = {}

    with open(filename) as f:
        instructions = [line.split() for line in f]

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers.update(initial)

    toggle = {
        "cpy": "jnz",
        "jnz": "cpy",
        "inc": "dec",
        "dec": "inc",
        "tgl": "inc",
    }

    def value(x):
        return int(x) if x.lstrip("-").isdigit() else registers[x]

    pc = 0

    while 0 <= pc < len(instructions):
        if (
            pc + 5 < len(instructions)
            and instructions[pc][0] == "cpy"
            and instructions[pc + 1][0] == "inc"
            and instructions[pc + 2][0] == "dec"
            and instructions[pc + 3] == ["jnz", instructions[pc + 2][1], "-2"]
            and instructions[pc + 4][0] == "dec"
            and instructions[pc + 5] == ["jnz", instructions[pc + 4][1], "-5"]
        ):
            src = instructions[pc][1]
            counter = instructions[pc + 4][1]
            dest = instructions[pc + 1][1]
            temp = instructions[pc + 2][1]

            registers[dest] += value(src) * registers[counter]
            registers[temp] = 0
            registers[counter] = 0

            pc += 6
            continue

        op, *args = instructions[pc]

        if op == "cpy":
            src, dst = args
            if dst in registers:
                registers[dst] = value(src)

        elif op == "inc":
            if args[0] in registers:
                registers[args[0]] += 1

        elif op == "dec":
            if args[0] in registers:
                registers[args[0]] -= 1

        elif op == "jnz":
            if value(args[0]) != 0:
                pc += value(args[1])
                continue

        elif op == "tgl":
            target = pc + value(args[0])

            if 0 <= target < len(instructions):
                instructions[target][0] = toggle[instructions[target][0]]

        pc += 1

    return registers["a"]


print(solve(initial={"a": 12}))
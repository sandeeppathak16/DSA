def solve(filename="25.txt", initial=None):
    if initial is None:
        initial = {}

    with open(filename) as f:
        instructions = [line.strip().split() for line in f]

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers.update(initial)

    def value(x):
        return int(x) if x.lstrip("-").isdigit() else registers[x]

    expected = 0
    visited = set()
    pc = 0

    while 0 <= pc < len(instructions):
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
            src, offset = args

            if value(src) != 0:
                pc += value(offset)
                continue

        elif op == "out":
            output = value(args[0])

            if output != expected:
                return False

            state = (pc, *registers.values())

            if state in visited:
                return True

            visited.add(state)

            expected = 1 - expected

        pc += 1

    return False


a = 0

while True:
    if solve(initial={"a": a}):
        print(a)
        break

    a += 1
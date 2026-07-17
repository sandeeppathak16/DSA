def solve(filename="12.txt", initial=None):
    if initial is None:
        initial = {}

    with open(filename) as f:
        instructions = [line.strip().split() for line in f]

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers.update(initial)

    i = 0

    while 0 <= i < len(instructions):
        op, *args = instructions[i]

        if op == "cpy":
            src, dst = args
            if dst in registers:
                registers[dst] = (
                    int(src)
                    if src.lstrip("-").isdigit()
                    else registers[src]
                )

        elif op == "inc":
            registers[args[0]] += 1

        elif op == "dec":
            registers[args[0]] -= 1

        elif op == "jnz":
            src, offset = args
            value = int(src) if src.lstrip("-").isdigit() else registers[src]

            if value != 0:
                i += int(offset)
                continue

        i += 1

    return registers["a"]

print(solve())
print(solve(initial={"c": 1}))
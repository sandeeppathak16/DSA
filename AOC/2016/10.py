from collections import defaultdict, deque
import re


VALUE_RE = re.compile(r"value (\d+) goes to bot (\d+)")
RULE_RE = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) "
    r"and high to (bot|output) (\d+)"
)


def solve(filename="10.txt"):
    bots = defaultdict(
        lambda: {
            "values": [],
            "instruction": None,
        }
    )

    outputs = defaultdict(list)
    ready = deque()

    with open(filename) as f:
        for line in f:
            line = line.strip()

            if m := VALUE_RE.match(line):
                value = int(m.group(1))
                bot = int(m.group(2))

                bots[bot]["values"].append(value)

                if len(bots[bot]["values"]) == 2:
                    ready.append(bot)

            else:
                m = RULE_RE.match(line)

                bot = int(m.group(1))

                bots[bot]["instruction"] = (
                    (m.group(2), int(m.group(3))),
                    (m.group(4), int(m.group(5))),
                )

                if len(bots[bot]["values"]) == 2:
                    ready.append(bot)

    part1 = None

    while ready:
        bot = ready.popleft()

        if len(bots[bot]["values"]) < 2:
            continue

        instruction = bots[bot]["instruction"]
        if instruction is None:
            continue

        low, high = sorted(bots[bot]["values"])
        bots[bot]["values"].clear()

        if low == 17 and high == 61:
            part1 = bot

        for (dest_type, dest_id), value in zip(
            instruction,
            (low, high),
        ):
            if dest_type == "bot":
                bots[dest_id]["values"].append(value)

                if len(bots[dest_id]["values"]) == 2:
                    ready.append(dest_id)
            else:
                outputs[dest_id].append(value)

    part2 = outputs[0][0] * outputs[1][0] * outputs[2][0]

    return part1, part2


part1, part2 = solve()

print("Part 1:", part1)
print("Part 2:", part2)






import re


TARGET_LOW = 17
TARGET_HIGH = 61


def process(bot, mapping):
    if len(mapping[bot]["values"]) < 2:
        return

    if not mapping[bot]["instructions"]:
        return

    v1 = mapping[bot]["values"].pop()
    v2 = mapping[bot]["values"].pop()

    low, high = sorted((v1, v2))

    if low == TARGET_LOW and high == TARGET_HIGH:
        mapping["answer"] = bot

    low_pass, high_pass = mapping[bot]["instructions"][0]

    for destination, value in ((low_pass, low), (high_pass, high)):
        if destination not in mapping:
            mapping[destination] = {
                "values": [value],
                "instructions": [],
            }
        else:
            mapping[destination]["values"].append(value)

            if (
                len(mapping[destination]["values"]) == 2
                and mapping[destination]["instructions"]
            ):
                process(destination, mapping)


def solve(filename="10.txt"):
    pattern = re.compile(
        r"^(?:value (\d+) goes to bot (\d+)|"
        r"bot (\d+) gives low to (bot|output) (\d+) "
        r"and high to (bot|output) (\d+))$"
    )

    instructions = []

    with open(filename) as f:
        for line in f:
            line = line.strip()

            match = pattern.match(line)
            if not match:
                continue

            instructions.append(match.groups())

    mapping = {"answer": None}

    for instruction in instructions:
        if instruction[0] is not None:
            bot = f"bot {instruction[1]}"
            value = int(instruction[0])

            if bot not in mapping:
                mapping[bot] = {
                    "values": [value],
                    "instructions": [],
                }
            else:
                mapping[bot]["values"].append(value)

            if (
                len(mapping[bot]["values"]) == 2
                and mapping[bot]["instructions"]
            ):
                process(bot, mapping)

        else:
            bot = f"bot {instruction[2]}"
            low_pass = f"{instruction[3]} {instruction[4]}"
            high_pass = f"{instruction[5]} {instruction[6]}"

            if bot not in mapping:
                mapping[bot] = {
                    "values": [],
                    "instructions": [[low_pass, high_pass]],
                }
            else:
                mapping[bot]["instructions"].append([low_pass, high_pass])

            if (
                len(mapping[bot]["values"]) == 2
                and mapping[bot]["instructions"]
            ):
                process(bot, mapping)

    part1 = mapping["answer"]

    part2 = (
        mapping["output 0"]["values"][0]
        * mapping["output 1"]["values"][0]
        * mapping["output 2"]["values"][0]
    )

    print("Part 1:", part1)
    print("Part 2:", part2)


solve()


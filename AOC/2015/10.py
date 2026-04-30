def look_and_say(sequence: str) -> str:
    n = len(sequence)
    result = []

    current_char = sequence[0]
    count = 1

    for i in range(1, n):
        if sequence[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = sequence[i]
            count = 1

    result.append(f"{count}{current_char}")

    return "".join(result)


def run_iterations(sequence: str, steps: int) -> str:
    for _ in range(steps):
        sequence = look_and_say(sequence)
    return sequence


input_string = "3113322113"

part1_result = run_iterations(input_string, 40)
print(f"Answer Part 1 -> {len(part1_result)}")

part2_result = run_iterations(part1_result, 10)
print(f"Answer Part 2 -> {len(part2_result)}")

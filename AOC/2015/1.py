


def solve(filename="1.txt"):
    with open(filename, "r") as file:
        inputs = file.readline().strip()

    mapping = {'(': 1, ')': -1}
    floor = 0
    first_basement_pos = None

    for i, ch in enumerate(inputs, start=1):
        floor += mapping.get(ch, 0)

        if floor == -1 and first_basement_pos is None:
            first_basement_pos = i

    return floor, first_basement_pos
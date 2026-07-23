import re

text = """
Disc #1 has 17 positions; at time=0, it is at position 15.
Disc #2 has 3 positions; at time=0, it is at position 2.
Disc #3 has 19 positions; at time=0, it is at position 4.
Disc #4 has 13 positions; at time=0, it is at position 2.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 5 positions; at time=0, it is at position 0.
"""

matches = re.findall(
    r"Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+)\.",
    text,
)


def solve(positions, extra_disc=None):
    button_pressed_at = 0

    if extra_disc:
        positions += extra_disc

    while True:
        reached_at_bottom = True

        for i, pos in enumerate(positions, start=button_pressed_at + 1):
            total_position, starting_position = pos
            total_position = int(total_position)
            starting_position = int(starting_position)

            capsule_reached_at = (starting_position + i) % total_position

            if capsule_reached_at != 0:
                reached_at_bottom = False
                break

        if not reached_at_bottom:
            button_pressed_at += 1
            continue

        return button_pressed_at


# Part 1
print(solve(matches))

# Part 2
print(solve(matches, extra_disc=[(11, 0)]))
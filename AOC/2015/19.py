import random


def solve(filename='19.txt'):
    with open(filename, 'r') as file:
        replacements = []
        molecule = ''

        for line in file:
            line = line.strip()
            if '=>' in line:
                a, b = line.split(' => ')
                replacements.append((a, b))
            elif line:
                molecule = line

    molecules = set()

    for a, b in replacements:
        for i in range(len(molecule)):
            if molecule[i:i + len(a)] == a:
                new_molecule = (
                    molecule[:i] + b + molecule[i + len(a):]
                )
                molecules.add(new_molecule)

    part1 = len(molecules)

    reversed_rules = [(b, a) for a, b in replacements]

    target = molecule
    original_target = molecule

    steps = 0

    while target != 'e':
        for src, dst in reversed_rules:
            if src in target:
                target = target.replace(src, dst, 1)
                steps += 1
                break
        else:
            random.shuffle(reversed_rules)
            target = original_target
            steps = 0

    part2 = steps

    return part1, part2
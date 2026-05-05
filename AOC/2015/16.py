def solve(filename='16.txt', part=1):
    mapping = {}

    with open(filename, 'r') as file:
        for line in file:
            sue, mfcsam = line.strip().split(':', maxsplit=1)
            _, sue_id = sue.strip().split(' ', maxsplit=1)

            mapping[sue_id] = {}

            for m in mfcsam.strip().split(','):
                name, number = m.strip().split(':', maxsplit=1)
                mapping[sue_id][name] = int(number.strip())

    check = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    for sue_id, values in mapping.items():
        match = True

        for key, value in values.items():

            if part == 1:
                if check[key] != value:
                    match = False
                    break

            else:
                if key in {'cats', 'trees'}:
                    if value <= check[key]:
                        match = False
                        break

                elif key in {'pomeranians', 'goldfish'}:
                    if value >= check[key]:
                        match = False
                        break

                else:
                    if check[key] != value:
                        match = False
                        break

        if match:
            return sue_id
        
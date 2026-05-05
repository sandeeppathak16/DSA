def generate(n, total):
    if n == 1:
        yield [total]
        return

    for i in range(total + 1):
        for rest in generate(n - 1, total - i):
            yield [i] + rest

def compute_totals(sample, ingredients, mapping):
    totals = {
        "capacity": 0,
        "durability": 0,
        "flavor": 0,
        "texture": 0
    }

    for i, amount in enumerate(sample):
        ing = ingredients[i]
        for prop in totals:
            totals[prop] += mapping[ing][prop] * amount

    for prop in totals:
        if totals[prop] < 0:
            totals[prop] = 0

    return totals

def compute_calories(sample, ingredients, mapping):
    total_calories = 0

    for i, amount in enumerate(sample):
        ing = ingredients[i]
        total_calories += mapping[ing]["calories"] * amount

    return total_calories

def compute_score(totals):
    score = 1
    for value in totals.values():
        score *= value
    return score

def solve(filename='15.txt', calorie_target=None):
    mapping = {}

    with open(filename, 'r') as file:
        for line in file:
            ingredient, properties = line.strip().split(':', 1)

            props = {}
            for p in properties.split(','):
                name, value = p.strip().split(' ')
                props[name] = int(value)

            mapping[ingredient] = props

    ingredients = list(mapping.keys())
    n = len(ingredients)

    ans = 0

    for sample in generate(n, 100):

        if calorie_target is not None:
            if compute_calories(sample, ingredients, mapping) != calorie_target:
                continue

        totals = compute_totals(sample, ingredients, mapping)
        score = compute_score(totals)

        ans = max(ans, score)

    return ans
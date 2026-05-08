def find_divisors_generator(n):
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i

            # Avoid duplicate divisor for perfect squares
            if i != n // i:
                yield n // i


def solve(number=36_000_000, multiplier=10, limit=None):
    """
    Part 1:
        multiplier = 10
        limit = None

    Part 2:
        multiplier = 11
        limit = 50
    """

    house_number = 1

    while True:
        presents = 0

        for d in find_divisors_generator(house_number):
            if limit is not None and house_number > d * limit:
                continue

            presents += d * multiplier

        if presents >= number:
            return house_number

        house_number += 1
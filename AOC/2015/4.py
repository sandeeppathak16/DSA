import hashlib

def solve(starting_zeroes):
    secret_key = 'bgvyzdsv'
    counter = 1

    while True:
        test_input = f"{secret_key}{counter}"

        hash_result = hashlib.md5(test_input.encode()).hexdigest()

        if hash_result.startswith(starting_zeroes):
            return counter

        counter += 1


def solve1():
    return solve('00000')


def solve2():
    return solve('000000')

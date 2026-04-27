def is_nice_part1(word):
    vowels = 'aeiou'

    vowel_count = sum(1 for ch in word if ch in vowels)
    if vowel_count < 3:
        return False

    if not any(word[i] == word[i+1] for i in range(len(word)-1)):
        return False

    if any(x in word for x in ['ab', 'cd', 'pq', 'xy']):
        return False

    return True


def is_nice_part2(word):
    pairs = {}
    pair_found = False

    for i in range(len(word) - 1):
        pair = word[i:i+2]
        if pair in pairs:
            if i - pairs[pair] > 1:
                pair_found = True
                break
        else:
            pairs[pair] = i

    if not pair_found:
        return False

    if not any(word[i] == word[i+2] for i in range(len(word) - 2)):
        return False

    return True


def solve(filename='5.txt'):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file]

    part1_count = 0
    part2_count = 0

    for word in words:
        if is_nice_part1(word):
            part1_count += 1

        if is_nice_part2(word):
            part2_count += 1

    return part1_count, part2_count


print(solve())


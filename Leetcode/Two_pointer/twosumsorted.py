numbers = [2 , 7, 11, 15]
target = 9


def twosumsorted(numbers, target):
    i = 0
    j = len(numbers) - 1

    while i < j:
        _sum = numbers[i] + numbers[j]

        if _sum == target:
            return [i + 1, j + 1]

        elif _sum > target:
            j -= 1

        else:
            i += 1


print(twosumsorted(numbers, target))
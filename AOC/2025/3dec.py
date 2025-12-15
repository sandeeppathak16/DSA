def find_joltage(numbers):
    maxN = int(numbers[0])
    maxI = 0

    for i in range(1, len(numbers) - 1):
        if int(numbers[i]) > maxN:
            maxN = int(numbers[i])
            maxI = i

    secMaxN = int(numbers[maxI + 1])
    for j in range(maxI + 1, len(numbers)):
        if secMaxN < int(numbers[j]):
            secMaxN = int(numbers[j])

    return int(f'{maxN}{secMaxN}')


def find_joltage_2(numbers):
    res = ""
    maxI = -1

    for i in range(12, 0, -1):
        maxN = float('-inf')
        best_pos = maxI

        for j in range(maxI + 1, len(numbers) - i + 1):
            if int(numbers[j]) > maxN:
                maxN = int(numbers[j])
                best_pos = j

        maxI = best_pos
        res += numbers[maxI]

    return int(res)


ans = 0

# codes = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']
# codes = ['987654321111111']

with open("3dec.txt", "r") as f:
    codes = [line.strip() for line in f.readlines()]

# for numbers in codes:
#     ans += find_joltage(numbers)

for numbers in codes:
    ans += find_joltage_2(numbers)

print(ans)  # 17405 ans

from collections import Counter


def decrypt(text, shift):
    shift %= 26

    result = []

    for ch in text:
        if ch == "-":
            result.append(" ")
        else:
            new_char = chr(
                (ord(ch) - ord('a') + shift) % 26 + ord('a')
            )
            result.append(new_char)

    return ''.join(result)


def solve(filename="4.txt"):
    part1 = 0
    part2 = None

    with open(filename) as f:
        for line in f:
            line = line.strip()

            checksum = line[-6:-1]

            name, sector_id = line[:-7].rsplit("-", 1)

            sector_id = int(sector_id)

            clean_name = name.replace("-", "")

            count = Counter(clean_name)

            count = sorted(
                count.items(),
                key=lambda x: (-x[1], x[0])
            )

            expected = ''.join(ch for ch, _ in count[:5])

            if expected == checksum:

                part1 += sector_id

                decrypted = decrypt(name, sector_id)

                if "northpole" in decrypted:
                    part2 = sector_id

    return part1, part2


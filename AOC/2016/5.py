import hashlib


def solve(part2=False):
    door_id = "ugkcyxxp"
    password = [""] * 8

    found = 0
    number = 0

    while found < 8:
        md5 = hashlib.md5(f"{door_id}{number}".encode()).hexdigest()

        if md5.startswith("00000"):

            if part2:
                pos = md5[5]

                if pos.isdigit():
                    pos = int(pos)

                    if pos < 8 and password[pos] == "":
                        password[pos] = md5[6]
                        found += 1
            else:
                password[found] = md5[5]
                found += 1

        number += 1

    return "".join(password)


print(solve(True))
def increment_password(pw):
    pw = list(pw)
    i = len(pw) - 1

    while i >= 0:
        if pw[i] == 'z':
            pw[i] = 'a'
            i -= 1
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break

    return ''.join(pw)


def has_straight(pw):
    for i in range(len(pw) - 2):
        if (ord(pw[i]) + 1 == ord(pw[i + 1]) and
            ord(pw[i]) + 2 == ord(pw[i + 2])):
            return True
    return False


def has_no_invalid_chars(pw):
    return all(c not in pw for c in ['i', 'o', 'l'])


def has_two_pairs(pw):
    pairs = set()
    i = 0
    while i < len(pw) - 1:
        if pw[i] == pw[i + 1]:
            pairs.add(pw[i])
            i += 2  # skip overlapping
        else:
            i += 1
    return len(pairs) >= 2


def is_valid(pw):
    return (
        has_straight(pw) and
        has_no_invalid_chars(pw) and
        has_two_pairs(pw)
    )


def find_next_password(pw):
    while True:
        pw = increment_password(pw)
        if is_valid(pw):
            return pw


current_password = "vzbxkghb"

next_password = find_next_password(current_password)
print("Next password:", next_password)
next_password = find_next_password(next_password)
print("Next to Next password:", next_password)
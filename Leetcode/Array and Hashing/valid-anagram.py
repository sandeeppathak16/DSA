
s = "anagram"
t = "nagaramdd"


def valid_anagram(s, t):
    counter = {}

    for ele in s:
        counter[ele] = counter.get(ele, 0) + 1

    for ele in t:
        if ele not in counter:
            return False

        counter[ele] -= 1

    for v in counter.values():

        if v != 0:
            return False

    return True


print(valid_anagram(s, t))
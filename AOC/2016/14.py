import hashlib


def generate_hash(salt, index, stretch_count):
    md5_hash = hashlib.md5(f"{salt}{index}".encode()).hexdigest()

    for _ in range(stretch_count):
        md5_hash = hashlib.md5(md5_hash.encode()).hexdigest()

    return md5_hash


def first_triplet(md5_hash):
    for i in range(len(md5_hash) - 2):
        if md5_hash[i:i + 3] == md5_hash[i] * 3:
            return md5_hash[i]
    return None


def solve(salt="yjdafjpo", hash_count=0):
    keys = []
    candidates = []
    index = 0

    while True:
        if len(keys) >= 64:
            keys.sort(key=lambda item: item[0])
            if index > keys[63][0] + 1000:
                break

        md5_hash = generate_hash(salt, index, hash_count)

        first_valid = 0
        while (
            first_valid < len(candidates)
            and candidates[first_valid][0] + 1000 < index
        ):
            first_valid += 1
        candidates = candidates[first_valid:]

        remove_indices = []

        for i, (candidate_index, character, candidate_hash) in enumerate(candidates):
            if character * 5 in md5_hash:
                keys.append((candidate_index, candidate_hash))
                remove_indices.append(i)

        for removed, candidate_index in enumerate(remove_indices):
            candidates.pop(candidate_index - removed)

        character = first_triplet(md5_hash)

        if character:
            candidates.append((index, character, md5_hash))

        index += 1

    return keys[63][0]


print(solve(hash_count=2016))
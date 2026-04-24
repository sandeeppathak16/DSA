strs = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(strs):
    from collections import defaultdict
    mapping = defaultdict(list)

    for s in strs:
        counter = [0] * 26

        for ch in s:
            counter[ord(ch) - ord('a')] += 1


        mapping[tuple(counter)].append(s)

    
    return list(mapping.values())


print(group_anagrams(strs))
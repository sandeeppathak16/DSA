nums = [2,7,11,15]
target = 9


def two_sum(nums, target):
    hashmap = {}

    for i, ele in enumerate(nums):
        t = target - ele

        if t in hashmap:
            return [hashmap[t], i]

        hashmap[ele] = i



print(two_sum(nums, target))
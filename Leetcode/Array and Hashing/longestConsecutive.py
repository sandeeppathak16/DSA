nums = [100, 4, 200, 1, 3, 2]


def longestConsecutive(nums):
    nums = set(nums)

    ans = 0

    for num in nums:
        if num - 1 not in nums:

            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_streak += 1
                current_num += 1

            
            ans = max(ans, current_streak)


    return ans


print(longestConsecutive(nums))
nums = [-1, 0, 1, 2, -1, -4]


def threesum(nums):
    nums.sort()
    ans = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            _sum = nums[i] + nums[j] + nums[k]

            if _sum > 0:
                k -= 1
            elif _sum < 0:
                j += 1
            
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                while j < k and nums[k] == nums[k + 1]:
                    k += 1

    
    return ans


print(threesum(nums))
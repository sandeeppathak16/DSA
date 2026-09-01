def longestOnes(nums):
    i = 0

    n = len(nums)
    zero_count = 0
    ans = 0

    for j in range(n):
        if nums[j] == 0:
            zero_count += 1

        
        while zero_count > k:
            if nums[i] == 0:
                zero_count -= 1

            i += 1

        ans = max(ans, j - i + 1)

    return ans
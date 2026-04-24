nums = [1, 2, 3, 4]



def productExceptSelf(nums):
    n = len(nums)

    prefix = [0 for _ in range(n)]
    postfix = [0 for _ in range(n)]

    prefix[0] = 1

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    
    postfix[-1] = 1

    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i + 1]

    
    return [postfix[i] * prefix[i] for i in range(n)]


print(productExceptSelf(nums))
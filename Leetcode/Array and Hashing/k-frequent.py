nums = [1,1,1,2,2,3] 
k = 2


def topKFrequent(nums, k):
    counter = {}

    for ele in nums:
        counter[ele] = counter.get(ele, 1) + 1

    
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in counter.items():
        bucket[freq].append(num)

    result = []
    
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)

            if len(result) == k:
                return result



print(topKFrequent(nums, k))
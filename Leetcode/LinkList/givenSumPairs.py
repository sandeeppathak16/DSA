def givenSumPairs(head, target):
    check = set()
    ans = []
    
    while head:
        r = target - head.data
        if r in check:
            ans.append([r, head.data])
            
        check.add(head.data)
        head = head.next
        
    return ans
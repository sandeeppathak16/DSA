def lengthOfLoop(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            ans = 1
            current = slow.next
            
            while slow != current:
                ans += 1
                current = current.next
                
            return ans
            
    return 0
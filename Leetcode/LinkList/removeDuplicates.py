def removeDuplicates(headRef):
    temp = headRef
    current = headRef
    
    while headRef:
        if headRef.data != current.data:
            current.next = headRef
            headRef.prev = current
            current = headRef
        
        headRef = headRef.next
        
    current.next = None
        
    return temp
            
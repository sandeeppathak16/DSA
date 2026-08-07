def addOne(head):
    def helper(temp):
        if temp is None:
            return 1
            
        carry = helper(temp.next)
        
        temp.data += carry
        
        if temp.data >= 10:
            temp.data = 0
            return 1
        
        return 0
        
    carry = helper(head)
    
    if carry == 1:
        new_node = Node(carry)
        new_node.next = head
        return new_node
        
    return head
            
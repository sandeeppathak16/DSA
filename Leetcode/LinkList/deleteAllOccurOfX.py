class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def deleteAllOccurOfX(head, x):
    ans = Node(0)
    prev = ans
    prev.next = head
    
    while head:
        if head.data == x:
            prev.next = head.next
            
            if head.next:
                head.next.prev = prev
        else:
            prev = head
            
        
        head = head.next
        
    
    return ans.next
                
            
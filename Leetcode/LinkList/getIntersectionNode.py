from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    temp1 = headA
    temp2 = headB

    while temp1 != temp2:
        if not temp1:
            temp1 = headB
        else:
            temp1 = temp1.next

        if not temp2:
            temp2 = headA
        else:
            temp2 = temp2.next

    return temp1

        

            
            
        
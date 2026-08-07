from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
            return head

    oddNode = head
    evenNode = head.next
    evenHead = evenNode

    while evenNode and evenNode.next:
        oddNode.next = evenNode.next
        evenNode.next = oddNode.next.next

        oddNode = oddNode.next
        evenNode = evenNode.next

    
    oddNode.next = evenHead

    return head
        
        
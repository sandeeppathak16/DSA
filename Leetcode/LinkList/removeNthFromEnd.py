from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head

        for _ in range(n):
            second = second.next

        if second is None:
            return head.next

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next

        return head
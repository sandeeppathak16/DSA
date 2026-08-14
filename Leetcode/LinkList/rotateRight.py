from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    t = head
    n = 0

    while t:
        n += 1
        t = t.next

    if not n:
        return head

    k = k % n

    if k == 0:
        return head

    dummy = ListNode(next=head)
    prev = dummy

    for _ in range(n - k):
        head = head.next
        prev = prev.next

    t = head
    while t.next:
        t = t.next

    prev.next = None
    t.next = dummy.next

    return head
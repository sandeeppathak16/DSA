from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)
    dummay = head
    c = 0

    while l1 or l2:
        s = c

        if l1:
            s += l1.val
            l1 = l1.next

        if l2:
            s += l2.val
            l2 = l2.next

        
        c = s // 10
        d = s % 10

        dummay.next = ListNode(d)
        dummay = dummay.next

    if c:
        dummay.next = ListNode(c)

    return head.next

        
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
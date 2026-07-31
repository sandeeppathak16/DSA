from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow


    return None
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    mid = self.findMid(head)
    midNext = mid.next

    mid.next = None

    left = self.sortList(head)
    right = self.sortList(midNext)

    return self.merge(left, right)

    
def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    if not left:
        return right
    
    if not right:
        return left

    if left.val < right.val:
        left.next = self.merge(left.next, right)
        return left
    else:
        right.next = self.merge(left, right.next)
        return right
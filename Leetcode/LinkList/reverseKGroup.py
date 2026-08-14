from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    groupprev = dummy

    while True:
        kth = getKth(groupprev, k)

        if not kth:
            break

        groupnext = kth.next
        prev, curr = kth.next, groupprev.next

        while curr != groupnext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        tmp = groupprev.next
        groupprev.next = kth
        groupprev = tmp

    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse(head):
        prev = None

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    n = 0
    temp = head

    while temp:
        n += 1
        temp = temp.next

    if n < k:
        return head

    first = second = head
    ans = None

    for _ in range(n // k):

        for _ in range(k - 1):
            second = second.next

        temp = second.next
        second.next = None

        node = reverse(first)

        if ans is None:
            ans = node
        else:
            t = ans
            while t.next:
                t = t.next
            t.next = node

        first = second = temp

    if first:
        t = ans
        while t.next:
            t = t.next
        t.next = first

    return ans


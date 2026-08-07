from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0

    check = head
    while check:
        count += 1
        check = check.next

    n = count // 2

    temp = head
    for i in range(n - 1):
        temp = temp.next
    
    if temp == None or temp.next == None:
        return head.next

    temp.next = temp.next.next

    return head
        
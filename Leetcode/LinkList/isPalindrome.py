def reverse(node):
    prev = None

    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    return prev

def isPalindrome(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    second = reverse(slow)

    first = head

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True
    
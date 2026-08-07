class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

        
def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next


    left_node = prev.next

    curr = left_node

    rev_node = None

    for _ in range(right - left + 1):
        temp = curr.next
        curr.next = rev_node
        rev_node = curr
        curr = temp

    prev.next = rev_node
    left_node.next = curr

    

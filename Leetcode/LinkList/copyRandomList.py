from typing import Optional

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    oldtonew = {None : None}

    curr = head 

    while curr:
        oldtonew[curr] = Node(curr.val)
        curr = curr.next

    curr = head

    while curr:
        node = oldtonew[curr]
        node.next = oldtonew[curr.next]
        node.random = oldtonew[curr.random]
        curr = curr.next

    return oldtonew[head]
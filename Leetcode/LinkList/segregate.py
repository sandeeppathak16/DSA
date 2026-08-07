def segregate(head):
    counter = {
        0: 0,
        1: 0,
        2: 0
    }
    
    temp = head
    
    while temp:
        counter[temp.data] += 1
        temp = temp.next
        
    temp = head
    for c, v in counter.items():
        
        for _ in range(v):
            temp.data = c
            temp = temp.next
            
    return head

# without Modifies 

def segregate(self, head):
    zero_dummy = Node(-1)
    one_dummy = Node(-1)
    two_dummy = Node(-1)

    zero = zero_dummy
    one = one_dummy
    two = two_dummy

    curr = head

    while curr:
        if curr.data == 0:
            zero.next = curr
            zero = zero.next
        elif curr.data == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next

        curr = curr.next

    zero.next = one_dummy.next if one_dummy.next else two_dummy.next
    one.next = two_dummy.next
    two.next = None

    return zero_dummy.next
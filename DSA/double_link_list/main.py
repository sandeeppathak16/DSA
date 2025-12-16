class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DDL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __repr__(self):
        string = ""
        if self.head is None:
            string += "Doubly Linked List Empty"
            return string

        string += f"Doubly Linked List:\n{self.head.data}"
        start = self.head.next
        while start != None:
            string += f" -> {start.data}"
            start = start.next
        return string

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return

        self.tail.next = Node(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.count += 1

    def insert(self, index, value):
        if index > self.count or index < 0:
            print("invalid Index")
            return

        if index == self.count:
            self.append(value)
            return

        if index == 0:
            self.head.prev = Node(value)
            self.head.prev.next = self.head
            self.head = self.head.prev
            self.count += 1
            return
        start = self.head
        for _ in range(index):
            start = start.next
        start.prev.next = Node(value)
        start.prev.next.prev = start.prev
        start.prev.next.next = start
        start.prev = start.prev.next
        self.count += 1

    def delete(self, index):
        if index > self.count or index < 0:
            print("invalid Index")
            return

        if index == self.count:
            self.tail = self.tail.prev
            self.tail.next = None
            self.count -= 1
            return

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return

        start = self.head
        for i in range(index):
            start = start.next

        start.prev.next = start.next
        start.next.prev = start.prev
        self.count -= 1


my_ddl = DDL()
my_ddl.append("B")
my_ddl.append("C")
my_ddl.append("D")
my_ddl.insert(3, "E")
my_ddl.insert(0, "ZERO")
my_ddl.insert(2, "two")
print(my_ddl)

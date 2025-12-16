class Node:
    def __init__(self, dataval=0):
        self.dataval = dataval
        self.nextval = None


class SLinkList:
    def __init__(self):
        self.headval = None

    def add_start(self, data):
        Newnode = Node(data)
        Newnode.nextval = self.headval
        self.headval = Newnode

    def add_last(self, data):
        Newnode2 = Node(data)
        if self.headval is None:
            self.headval = Newnode2
            return
        link = self.headval
        while link.nextval is not None:
            link = link.nextval
        link.nextval = Newnode2

    def add_in(self, node, data):
        newnode = Node(data)

        newnode.nextval = node.nextval
        node.nextval = newnode

    def remove_v(self, data):
        head = self.headval

        if head is not None:
            if head.dataval == data:
                self.headval = head.nextval
                head = None
                return
        while head is not None:
            if head.dataval == data:
                break
            prev = head
            head = head.nextval
        if (head == None):
            return

        prev.nextval = head.nextval
        head = None

    def printLink(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


My_link = SLinkList()

My_link.headval = Node("A")
N2 = Node("B")
N3 = Node("C")
My_link.headval.nextval = N2
N2.nextval = N3
My_link.add_start("1")
My_link.add_start("2")
My_link.add_last("d")
My_link.add_last("e")
My_link.add_in(N3, "K")
My_link.remove_v("1")
My_link.printLink()

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value

    def find(self, value):
        if value > self.data:
            if self.right is None:
                print("Not Found")
                return
            else:
                self.right.find(value)
        elif value < self.data:
            if self.left is None:
                print("Not Found")
                return
            else:
                self.left.find(value)
        else:
            print("Found")

    def min_val(self):
        left_node = self
        while left_node.left:
            left_node = left_node.left
        return left_node.data

    def max_val(self):
        right_node = self
        while right_node.right:
            right_node = right_node.right
        return right_node.data


my_node = Node(12)
my_node.insert(13)
my_node.insert(6)
my_node.insert(19)
my_node.insert(11)
my_node.find(11)
print(my_node.min_val())
print(my_node.max_val())

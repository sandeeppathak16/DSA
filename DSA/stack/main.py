class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):

        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

    def remove(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            return self.stack.pop()


my_stack = Stack()

my_stack.push("sandeep")
my_stack.push("Pathak")
my_stack.remove()
print(my_stack.peek())

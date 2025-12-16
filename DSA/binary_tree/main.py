class BTree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if self.data is not None:
            if value < self.data:
                if self.left is None:
                    self.left = BTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BTree(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)


my_btree = BTree(12)
my_btree.insert(10)
my_btree.insert(14)
my_btree.insert(0)
my_btree.insert(101)
my_btree.printTree()

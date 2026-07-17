class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        self.size += 1

    def pop_left(self):
        if self.size == 0:
            return None

        node = self.left.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}       
        self.freq_map = {}
        self.min_freq = 0

    def update_frequency(self, node):
        freq = node.freq

        dll = self.freq_map[freq]
        dll.remove(node)

        if freq == self.min_freq and dll.size == 0:
            self.min_freq += 1

        node.freq += 1

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()

        self.freq_map[node.freq].insert(node)

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.update_frequency(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.update_frequency(node)
            return

        if len(self.cache) == self.capacity:
            dll = self.freq_map[self.min_freq]
            node = dll.pop_left()
            del self.cache[node.key]

        node = Node(key, value)

        self.min_freq = 1

        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()

        self.freq_map[1].insert(node)
        self.cache[key] = node
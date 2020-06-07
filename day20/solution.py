class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy
        self.before = None
        self.current = None

    def after(self):
        self.current = self.head
        print('after >> ', self.current.data)

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node


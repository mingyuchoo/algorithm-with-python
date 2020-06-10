class Node:
    def __init__(self, target):
        self.data = target
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, target) -> Node:
        new_node = Node(target)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return self.head

    def traversal(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def find(self, target) -> bool:
        result = False
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return result

    def delete(self, target):
        current = self.head
        if current.data == target:
            self.head = current.next
            return current
        else:
            while current:
                if current.next.data == target:
                    next_next_node = current.next.next
                    current.next = next_next_node
                    return current.next
                current = current.next

    def sort(self):
        current = self.head
        next_node = current.next
        if current.data > next_node.data:
            current.next = next_node.next
            next_node.next = current
            self.head = next_node

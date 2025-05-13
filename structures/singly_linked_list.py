class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result[::-1]
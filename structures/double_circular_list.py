class CircularDoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class DoubleCircularList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = CircularDoubleNode(data)
        if not self.head:
            self.head = node
            node.next = node.prev = node
        else:
            tail = self.head.prev
            tail.next = node
            node.prev = tail
            node.next = self.head
            self.head.prev = node

    def to_list(self):
        result = []
        if not self.head:
            return result
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result
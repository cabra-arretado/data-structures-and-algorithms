class Node:
    value = None
    previous = None

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    tail = None
    length = 0

    def push(self, item):
        new_node = Node(item)
        self.length += 1
        if self.tail is None:
            self.tail = new_node
            return
        new_node.previous = self.tail
        self.tail = new_node

    def pop(self):
        if self.tail is None:
            return None
        self.length -= 1
        value = self.tail.value
        self.tail = self.tail.previous
        return value



    def peek(self):
        if self.tail:
            return self.tail.value


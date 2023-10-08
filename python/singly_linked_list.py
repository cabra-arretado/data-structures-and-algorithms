class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    head = None
    length = 0

    def __init__(self):
        self.head = None

    def __len__(self):
        return self.length

    def __str__(self):
        curr = self.head
        arr = []
        while (curr):
            arr.append(curr.value)
            curr = curr.next
        return str(arr)

    def _init_from_list(self, arr):
        """ Just for the tests """
        for val in arr:
            self.append(val)

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        last_node = self.head
        while (last_node.next):
            last_node = last_node.next
        last_node.next = new_node
        self.length += 1

    def prepend(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at(self, val, index):
        if index > self.length or index < 0 or not self.head:
            return
        if index == 0:
            self.prepend(val)
            return
        if index == self.length:
            self.append(val)
            return
        new_node = Node(val)
        prev_node = self.__get_node(index - 1)
        curr_node = prev_node.next
        prev_node.next = new_node
        new_node.next = curr_node
        self.length += 1

    def remove_at(self, index):
        if index > self.length or index < 0 or not self.head:
            return
        if index == 0:
            node = self.head
            self.head = self.head.next
            self.length -= 1
            return node.value
        prev_node = self.__get_node(index - 1)
        node = prev_node.next
        prev_node.next = prev_node.next.next
        self.length -= 1
        return node.value

    def __get_node(self, index) -> Node:
        if index > self.length or index < 0 or not self.head:
            return None
        if index == 0:
            return self.head
        curr = self.head
        count = 0
        while (count < index):
            curr = curr.next
            count += 1
            if not curr:
                return
        return curr

    def get(self, index):
        node = self.__get_node(index)
        if node:
            return node.value

    def remove(self, val):
        curr = self.head
        if not curr:
            return
        for i in range(self.length): 
            if not curr:
                return
            if curr.value == val:
                return self.remove_at(i)
            curr = curr.next

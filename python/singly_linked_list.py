class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	head = None
	length = 0

	def __init__(self):
		self.head = None

	def append(self, val):
		new_node = Node(val)
		if self.head is None:
			self.head = new_node
			return
		last_node = self.head
		while (last_node.next):
			last_node.next = last_node
		last_node.next = new_node
		self.length += 1
	
	def prepend(self, val):
		pass

	def insert_at(self, val, index):
		pass

	def remove_at(self, val, index):
		pass
    
	def get(index):
		pass

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

	def append(self, val):
		new_node = Node(val)

		if self.head is None:
			self.head = new_node
			self.length += 1
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
    
	def get(self, index):
		pass
	
	def remove(self, val):
		pass

if __name__ == "__main__":
	# Tests
	print("Running tests...")
	list = SinglyLinkedList()

	list.append(1)
	# [1]
	assert list.head.value == 1
	assert list.length == 1

	list.append(2)
	# [1, 2]
	assert list.head.value == 1
	assert list.head.value == 2
	assert list.get(1) == 2
	print("test append passed")

	list.prepend('a')
	# ['a', 1, 2]
	assert list.head.value == 'a'
	assert list.head.next.value == 1
	assert len(list) == 3
	print("test prepend passed")


	list.insert_at('b', 1)
	# ['a', 'b', 1, 2]
	assert list.head.value == 'a'
	assert len(list) == 4
	list.insert_at('z', 0)
	# ['z', 'a', 'b', 1, 2]
	assert list.head.value == 'z'
	assert len(list) == 5
	print("test insert_at passed")

	assert list.remove_at(1) == 'a'
	# ['z', 'b', 1, 2]
	assert list.head.value == 'z'
	assert len(list) == 4
	# ['b', 1, 2]
	assert list.remove_at(0) == 'z'
	assert list.head.value == 'b'
	assert len(list) == 3
	print("test remove_at passed")

	assert list.remove(1) == 1
	# ['b', 2]
	assert len(list) == 2
	assert list.head.value == 'b'
	assert list.append(3)
	assert list.append(4)
	# ['b', 2, 3, 4]
	assert list.get(2) == 3
	assert list.get(0) == 'b'
	print("test get passed")

	

	print("remove_at, insert_at, remove, get tests passed")

	



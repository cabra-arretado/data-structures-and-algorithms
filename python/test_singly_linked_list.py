from singly_linked_list import SinglyLinkedList
import unittest

class SLLTest(unittest.TestCase):
    sll = SinglyLinkedList()

    def test_append(self):
        self.sll.append(1)
        # [1]
        self.assertEqual(self.sll.head.value, 1)
        self.assertEqual(self.sll.length, 1)

        self.sll.append(2)
        # [1, 2]
        self.assertEqual(self.sll.head.value, 1)
        self.assertEqual(self.sll.get(1), 2)

    def test_prepend(self):
        self.sll.prepend('a')
        # # ['a', 1, 2]
        self.assertEqual(self.sll.head.value, 'a')
        self.assertEqual(self.sll.head.next.value, 1)
        self.assertEqual(len(self.sll), 3)

    def test_insert_at(self):
        self.sll.insert_at('b', 1)
        # ['a', 'b', 1, 2]
        self.assertEqual(self.sll.head.value, 'a')
        self.assertEqual(len(self.sll), 4)
        self.sll.insert_at('z', 0)
        # ['z', 'a', 'b', 1, 2]
        self.assertEqual(self.sll.head.value, 'z')
        self.assertEqual(len(self.sll), 5)

    # def test_remove_at(self):
    #     assert self.sll.remove_at(1) == 'a'
    #     # ['z', 'b', 1, 2]
    #     assert self.sll.head.value == 'z'
    #     assert len(self.sll) == 4
    #     # ['b', 1, 2]
    #     assert self.sll.remove_at(0) == 'z'
    #     assert self.sll.head.value == 'b'
    #     assert len(self.sll) == 3
    #     print("test remove_at passed")

    # def test_remove(self):
    #     assert self.sll.remove(1) == 1
    #     # ['b', 2]
    #     assert len(self.sll) == 2
    #     assert self.sll.head.value == 'b'
    #     self.sll.append(3)
    #     self.sll.append(4)
    #     # ['b', 2, 3, 4]
    #     assert self.sll.get(2) == 3
    #     assert self.sll.get(0) == 'b'

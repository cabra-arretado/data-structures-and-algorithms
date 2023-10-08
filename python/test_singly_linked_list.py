from singly_linked_list import SinglyLinkedList
import unittest


class SLLTest(unittest.TestCase):

    def test_append(self):
        sll = SinglyLinkedList()
        sll.append(1)
        # [1]
        self.assertEqual(sll.head.value, 1)
        self.assertEqual(sll.length, 1)

        sll.append(2)
        # [1, 2]
        self.assertEqual(sll.head.value, 1)
        self.assertEqual(sll.get(1), 2)

    def test_prepend(self):
        sll = SinglyLinkedList()
        sll._init_from_list([1, 2])
        sll.prepend('a')
        # # ['a', 1, 2]
        self.assertEqual(sll.head.value, 'a')
        self.assertEqual(sll.head.next.value, 1)
        self.assertEqual(len(sll), 3)

    def test_insert_at(self):
        sll = SinglyLinkedList()
        sll._init_from_list(['a', 1, 2])

        sll.insert_at('b', 1)
        # ['a', 'b', 1, 2]
        self.assertEqual(sll.head.value, 'a')
        self.assertEqual(len(sll), 4)
        sll.insert_at('z', 0)
        # ['z', 'a', 'b', 1, 2]
        self.assertEqual(sll.head.value, 'z')
        self.assertEqual(len(sll), 5)

    def test_remove_at(self):
        sll = SinglyLinkedList()
        sll._init_from_list(['z', 'a', 'b', 1, 2])
        self.assertEqual(sll.remove_at(1), 'a')
        # ['z', 'b', 1, 2]
        self.assertEqual(sll.head.value, 'z')
        self.assertEqua(len(sll), 4)
        # ['b', 1, 2]
        self.assertEqual(sll.remove_at(0), 'z')
        self.assertEqual(sll.head.value, 'b')
        self.assertEqual(len(sll), 3)

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

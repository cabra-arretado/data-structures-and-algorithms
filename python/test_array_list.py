import unittest

from array_list import ArrayList


class TestArrayList(unittest.TestCase):
    def test_append(self):
        array = ArrayList()

        array.append(1)
        self.assertEqual(1, array[0])
        self.assertEqual(len(array), 1)
        self.assertEqual(array.capacity, 5)

        array.append(2)
        self.assertEqual(1, array[0])
        self.assertEqual(len(array), 2)
        self.assertEqual(array.capacity, 5)

if __name__ == '__main__':
    unittest.main()

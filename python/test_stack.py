from stack import Stack
import unittest

class StackTest(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()

        # Push some items onto the stack
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # Pop the items off the stack and verify that they are in the correct order
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

        # Verify that the stack is now empty
        self.assertEqual(stack.pop(), None)

    def test_peek(self):
        stack = Stack()

        # Push some items onto the stack
        stack.push(1)
        stack.push(2)
        stack.push(3)

        # Peek at the top item on the stack
        self.assertEqual(stack.peek(), 3)

        # Pop the item off the stack and verify that it is the same as the peeked item
        self.assertEqual(stack.pop(), 3)

        # Peek at the top item on the stack again
        self.assertEqual(stack.peek(), 2)

    def test_empty_stack(self):
        stack = Stack()

        # Verify that the stack is empty
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.peek(), None)

if __name__ == '__main__':
    unittest.main()

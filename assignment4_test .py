import unittest
from assignment4 import UniqueStack, LimitedStack, RotatingStack


class UniqueStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_base_stack_empty(self):
        test_stack = UniqueStack()
        self.assertEqual(0, test_stack.size())

    def test_push_increases_size(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = UniqueStack()
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_peek_size_remains(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueStackTestCase.ITEM_1)
        self.assertEqual(UniqueStackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = UniqueStack()
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_pop_empty_stack(self):
        test_stack = UniqueStack()
        self.assertEqual(None, test_stack.pop())

    def test_repeat_stack(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueStackTestCase.ITEM_1)
        test_stack.push(UniqueStackTestCase.ITEM_2)
        test_stack.pop()
        test_stack.push(UniqueStackTestCase.ITEM_2)
        with self.assertRaises(ValueError):
            test_stack.push(UniqueStackTestCase.ITEM_1)
        self.assertEqual(2, test_stack.size())

    def test_pop_single_item(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueStackTestCase.ITEM_1)
        self.assertEqual(UniqueStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    def test_last_in_first_out(self):
        test_stack = UniqueStack()
        test_stack.push(UniqueStackTestCase.ITEM_1)
        test_stack.push(UniqueStackTestCase.ITEM_2)
        test_stack.push(UniqueStackTestCase.ITEM_3)
        self.assertEqual(3, test_stack.size())

        self.assertEqual(UniqueStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(UniqueStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(UniqueStackTestCase.ITEM_1, test_stack.pop())


class LimitedStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_base_stack_empty(self):
        test_stack = LimitedStack(10)
        self.assertEqual(0, test_stack.size())

    def test_push_increases_size(self):
        test_stack = LimitedStack(10)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    def test_peek_size_remains(self):
        test_stack = LimitedStack(10)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        self.assertEqual(LimitedStackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = LimitedStack(10)
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_pop_empty_stack(self):
        test_stack = LimitedStack(10)
        self.assertEqual(None, test_stack.pop())

    def test_pop_single_item(self):
        test_stack = LimitedStack(10)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        self.assertEqual(LimitedStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    def test_last_in_first_out(self):
        test_stack = LimitedStack(10)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        test_stack.push(LimitedStackTestCase.ITEM_2)
        test_stack.push(LimitedStackTestCase.ITEM_3)
        self.assertEqual(3, test_stack.size())

        self.assertEqual(LimitedStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(LimitedStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(LimitedStackTestCase.ITEM_1, test_stack.pop())

    def test_limit_stack(self):
        test_stack = LimitedStack(1)
        test_stack.push(LimitedStackTestCase.ITEM_1)
        with self.assertRaises(LimitedStack.LimitedStackOverflowError):
            test_stack.push(LimitedStackTestCase.ITEM_2)
            self.assertEqual(1, test_stack.size())

    def test_negative_stack(self):
        with self.assertRaises(ValueError):
            test_stack = LimitedStack(-1)

    def test_no_int_stack(self):
        with self.assertRaises(TypeError):
            test_stack = LimitedStack("hello")
            test_stack = LimitedStack(1.1)


class RotatingStackTestCase(unittest.TestCase):
    ITEM_1 = "item1"
    ITEM_2 = "item2"
    ITEM_3 = "item3"

    def test_base_stack_empty(self):
        test_stack = RotatingStack(10)
        self.assertEqual(0, test_stack.size())

    def test_push_increases_size(self):
        test_stack = RotatingStack(10)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        self.assertEqual(1, test_stack.size())

    def test_peek_size_remains(self):
        test_stack = RotatingStack(10)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        self.assertEqual(RotatingStackTestCase.ITEM_1, test_stack.peek())
        self.assertEqual(1, test_stack.size())

    def test_push_none(self):
        test_stack = RotatingStack(10)
        with self.assertRaises(TypeError):
            test_stack.push(None)

    def test_pop_empty_stack(self):
        test_stack = RotatingStack(10)
        self.assertEqual(None, test_stack.pop())

    def test_pop_single_item(self):
        test_stack = RotatingStack(10)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        self.assertEqual(RotatingStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())

    def test_last_in_first_out(self):
        test_stack = RotatingStack(10)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        test_stack.push(RotatingStackTestCase.ITEM_2)
        test_stack.push(RotatingStackTestCase.ITEM_3)
        self.assertEqual(3, test_stack.size())

        self.assertEqual(RotatingStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(RotatingStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(RotatingStackTestCase.ITEM_1, test_stack.pop())

    def test_negative_stack(self):
        with self.assertRaises(ValueError):
            test_stack = RotatingStack(-1)

    def test_no_int_stack(self):
        with self.assertRaises(TypeError):
            test_stack = RotatingStack("hello")
            test_stack = RotatingStack(1.1)

    def test_rotating(self):
        test_stack = RotatingStack(3)

        # try to rewrite one item
        test_stack.push(RotatingStackTestCase.ITEM_1)
        test_stack.push(RotatingStackTestCase.ITEM_2)
        test_stack.push(RotatingStackTestCase.ITEM_3)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        self.assertEqual(3, test_stack.size())
        self.assertEqual(RotatingStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(RotatingStackTestCase.ITEM_3, test_stack.pop())
        self.assertEqual(RotatingStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(0, test_stack.size())

        # try to rewrite two items
        test_stack.push(RotatingStackTestCase.ITEM_1)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        test_stack.push(RotatingStackTestCase.ITEM_1)
        test_stack.push(RotatingStackTestCase.ITEM_2)
        test_stack.push(RotatingStackTestCase.ITEM_2)
        self.assertEqual(3, test_stack.size())
        self.assertEqual(RotatingStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(RotatingStackTestCase.ITEM_2, test_stack.pop())
        self.assertEqual(RotatingStackTestCase.ITEM_1, test_stack.pop())
        self.assertEqual(0, test_stack.size())


if __name__ == '__main__':
    unittest.main()

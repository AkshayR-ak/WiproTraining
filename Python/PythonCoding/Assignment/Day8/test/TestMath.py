import unittest

from src.source import add, subtract, divide

# 1. Basic Test Case
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


# 2. Setup and Teardown
class TestList(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def tearDown(self):
        print("Test completed")

    def test_length(self):
        self.assertEqual(len(self.data), 3)


# 3. Multiple Assertions
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isupper(self):
        self.assertFalse("hello".isupper())


# 4. Exception Testing
class TestException(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


# 5. Test Suite Execution
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)


class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)



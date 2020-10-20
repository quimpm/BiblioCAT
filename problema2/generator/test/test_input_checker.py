import unittest
from src.input_checker import *

class TestInputChecker(unittest.TestCase):

    def setUp(self):
        self.checker = Checker(100, 100000, 1000, 10, 6, 10)

    def test_create_book(self):
        self.assertEqual(Book(0,3,4), createBook("B 0 3 4"))

    def test_create_library(self):
        self.assertEqual(Library(4,[1,2,3,4,0]), createLibrary("L 4 1 2 3 4 0"))

    def test_create_reader(self):
        self.assertEqual(Reader(0,4,[(8342, 3), (232, 5)]), createReader("R 0 4 8342 3 232 5"))

    def test_check_library(self):
        self.assertTrue(self.checker.checkLibrary(Library(4,[1,2,3,4,0])))
        self.assertFalse(self.checker.checkLibrary(Library(-1,[1,2,3,4,0])))
        self.assertFalse(self.checker.checkLibrary(Library(100000000,[1,2,3,4,0])))
        self.assertFalse(self.checker.checkLibrary(Library(4,[20,2,3,4,0])))
        self.assertFalse(self.checker.checkLibrary(Library(4,[])))

    def test_check_book(self):
        self.assertTrue(self.checker.checkBook(Book(0,3,4)))
        self.assertFalse(self.checker.checkBook(Book(100000,3,4)))
        self.assertFalse(self.checker.checkBook(Book(-1,3,4)))
        self.assertFalse(self.checker.checkBook(Book(0,11,4)))
        self.assertFalse(self.checker.checkBook(Book(0,0,4)))
        self.assertFalse(self.checker.checkBook(Book(0,3,101)))
        self.assertFalse(self.checker.checkBook(Book(0,3,-1)))


    def test_check_reader(self):
        self.assertTrue(self.checker.checkReader(Reader(0,4,[(8342, 3), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(1001,4,[(8342, 3), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(-1,4,[(8342, 3), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(0,100,[(8342, 3), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(0,-1,[(8342, 3), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(0,4,[(100000, 3), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(0,4,[(8342, 11), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(0,4,[(8342, 11), (232, 5)])))
        self.assertFalse(self.checker.checkReader(Reader(0,4,[(8342, 11), (232, 5), (8342, 11)])))
        self.assertFalse(self.checker.checkReader(Reader(0,4,[])))

    


if __name__ == "__main__":
    unittest.main()

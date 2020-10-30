import unittest
from src.utils.checker.BookChecker import *
from src.utils.checker.LibraryChecker import *
from src.utils.checker.ReaderChecker import *
from src.utils.checker.TimeChecker import *
from src.utils.parser.BookParser import *
from src.utils.parser.LibraryParser import *
from src.utils.parser.ReaderParser import *
from src.utils.parser.TimeParser import *
from src.gen_benchmark import *

class TestInputChecker(unittest.TestCase):

    def setUp(self):
        self.bookdata = BooksData(100000, 10)
        self.readerdata = ReaderData(1000, 10)
        self.num_of_libraries = 100
        self.time = 6

    def test_create_book(self):
        parser = BookParser()
        self.assertEqual(Book(0,3,4), parser.parse("B 0 3 4"))

    def test_create_library(self):
        parser = LibraryParser()
        self.assertEqual(Library(4,[1,2,3,4,0]), parser.parse("L 4 1 2 3 4 0"))

    def test_create_reader(self):
        parser = ReaderParser()
        self.assertEqual(Reader(0,4,[(8342, 3), (232, 5)]), parser.parse("R 0 4 8342 3 232 5"))

    def test_create_time(self):
        parser = TimeParser()
        self.assertEqual(6 , parser.parse("T 6"))

    def test_check_library(self):
        checker = LibraryChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)
        self.assertTrue(checker.check(Library(4,[1,2,3,4,0])))
        self.assertFalse(checker.check(Library(-1,[1,2,3,4,0])))
        self.assertFalse(checker.check(Library(100000000,[1,2,3,4,0])))
        self.assertFalse(checker.check(Library(4,[20,2,3,4,0])))
        self.assertFalse(checker.check(Library(4,[])))

    def test_check_book(self):
        checker = BookChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)
        self.assertTrue(checker.check(Book(0,3,4)))
        self.assertFalse(checker.check(Book(100000,3,4)))
        self.assertFalse(checker.check(Book(-1,3,4)))
        self.assertFalse(checker.check(Book(0,11,4)))
        self.assertFalse(checker.check(Book(0,0,4)))
        self.assertFalse(checker.check(Book(0,3,101)))
        self.assertFalse(checker.check(Book(0,3,-1)))


    def test_check_reader(self):
        checker = ReaderChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)
        self.assertTrue(checker.check(Reader(0,4,[(8342, 3), (232, 5)])))
        self.assertFalse(checker.check(Reader(1001,4,[(8342, 3), (232, 5)])))
        self.assertFalse(checker.check(Reader(-1,4,[(8342, 3), (232, 5)])))
        self.assertFalse(checker.check(Reader(0,100,[(8342, 3), (232, 5)])))
        self.assertFalse(checker.check(Reader(0,-1,[(8342, 3), (232, 5)])))
        self.assertFalse(checker.check(Reader(0,4,[(100000, 3), (232, 5)])))
        self.assertFalse(checker.check(Reader(0,4,[(8342, 11), (232, 5)])))
        self.assertFalse(checker.check(Reader(0,4,[(8342, 11), (232, 5)])))
        self.assertFalse(checker.check(Reader(0,4,[(8342, 11), (232, 5), (8342, 11)])))
        self.assertFalse(checker.check(Reader(0,4,[])))

    def test_check_time(self):
        checker = TimeChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)
        self.assertTrue(checker.check(6))
        self.assertFalse(checker.check(0))


if __name__ == "__main__":
    unittest.main()

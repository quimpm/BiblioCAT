#!/usr/bin/env python3

import unittest

from src.reader import Reader
from src.book import Book


class ReaderTest(unittest.TestCase):
    """
    Reader Test
    """

    def setUp(self):
        self.book_data = {0: 5, 1: 2, 3: 3}
        self.reader = Reader(books=self.book_data, location=1, max_weeks=6)
        self.books = [Book(1, 0, 3), Book(0, 1, 5), Book(1, 2, 4), Book(1, 3, 2)]

    def test_creation(self):
        """
        Tests the creation of a reader.
        """
        self.assertEqual(self.book_data, self.reader._books)
        self.assertEqual(1, self.reader._location)
        self.assertEqual([0, 0, 0, 0, 0, 0], self.reader._timing)

    def test_read(self):
        """
        Test simple read book 0.
        """
        self.reader._timing = [3, 2, 2, 1, 1, 1]
        score, time = self.reader.read(self.books[0], 0)
        self.assertEqual(3, score)
        self.assertEqual(6, time)
        self.assertEqual([3, 3, 3, 2, 2, 2], self.reader._timing)
        score, time = self.reader.read(self.books[3], 4)
        self.assertEqual(0, score)
        self.assertEqual(7, time)
        self.assertEqual([3, 3, 3, 2, 3, 3], self.reader._timing)

    def test_read_not_interested(self):
        """
        Test if Reader is not interested in books
        """
        try:
            self.reader.read(self.books[2], 0)
            self.fail("Readed book not interested")
        except AssertionError:
            pass

    def test_read_different_location(self):
        """
        Test if Book is in different location.
        """
        try:
            self.reader.read(self.books[1], 0)
            self.fail("Readed book was not in the library")
        except AssertionError:
            pass

#!/usr/bin/env python3

import unittest

from src.book import Book


class BookTest(unittest.TestCase):
    """
    Reader test
    """

    def setUp(self):
        self.book = Book(0, 1, 3)
        self.book2 = Book(1, 0, 3)

    def test_reader_creation(self):
        """
        Tests reader creation
        """
        self.assertEqual(0, self.book._location)
        self.assertEqual(1, self.book.id_book)
        self.assertEqual(0, self.book._internal_time)
        self.assertEqual(1, self.book2._location)
        self.assertEqual(0, self.book2.id_book)
        self.assertEqual(0, self.book2._internal_time)

    def test_move(self):
        """
        Tests move action
        """

        self.assertEqual(0, self.book._location)
        self.book.move(1, 5)
        self.assertEqual(1, self.book._location)
        self.assertEqual(5, self.book._internal_time)
        self.book.move(0, 3)
        self.assertEqual(0, self.book._location)
        self.assertEqual(8, self.book._internal_time)

    def test_read(self):
        """
        Test read action
        """
        self.assertEqual(0, self.book._internal_time)
        self.book.read(3)
        self.assertEqual(3, self.book._internal_time)
        self.book.read(5)
        self.assertEqual(5, self.book._internal_time)
        try:
            self.book.read(1)
            self.fail()
        except AssertionError:
            pass

    def test_move_then_read(self):
        """
        Tests move and then read
        """
        self.assertEqual(0, self.book._internal_time)
        self.book.move(1, 5)
        self.assertEqual(1, self.book._location)
        self.assertEqual(5, self.book._internal_time)
        self.book.read(8)
        self.assertEqual(8, self.book._internal_time)

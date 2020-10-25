#!/usr/bin/env python3

"""
Tests input parser
"""
import unittest

from src.parse_input import InputParser
from src.book import Book
from src.reader import Reader
from src.state import State


class InputParserTest(unittest.TestCase):
    """
    Input parser test case
    """

    def setUp(self):
        self.input_str = (
            "L 0 0 2 3"
            + "\nL 1 3 0 4"
            + "\nL 2 3 4 0"
            + "\nB 0 0 5"
            + "\nB 1 0 3"
            + "\nB 2 1 10"
            + "\nB 3 2 2"
            + "\nB 4 2 8"
            + "\nR 0 0 0 10 1 2"
            + "\nR 1 0 1 1 2 10 3 3"
            + "\nR 2 1 0 1 1 1 2 1 3 1 4 1"
            + "\nR 3 2 2 5 4 5"
        )

    def test_input_parser(self):
        ip = InputParser()
        for line in self.input_str.split("\n"):
            ip.parse_line(line)

        st = ip.get_state()
        trans = [[0, 2, 3], [3, 0, 4], [3, 4, 0]]
        books = [
            Book(0, 0, 5),
            Book(1, 0, 3),
            Book(2, 1, 10),
            Book(3, 2, 2),
            Book(4, 2, 8),
        ]
        readers = [
            Reader({0: 10, 1: 2}, 0, 12),
            Reader({1: 1, 2: 10, 3: 3}, 0, 12),
            Reader({0: 1, 1: 1, 2: 1, 3: 1, 4: 1}, 1, 12),
            Reader({2: 5, 4: 5}, 2, 12),
        ]
        expected = State(trans, books, readers)
        self.assertEqual(trans, st._transition)
        self.assertEqual(books, st._books)
        self.assertEqual(readers, st._readers)
        self.assertEqual(0, st._score)
        self.assertEqual(expected, st)

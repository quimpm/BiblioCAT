#!/usr/bin/env python3
"""
Reader class declaration.
"""
from typing import List, Dict, Tuple
from collections import namedtuple

from src.book import Book

time = int


class Reader:
    """
    Reprensents the state of a reader at a state.
    """

    _books: Dict[int, time]
    _location: int
    _timing: List[int]

    def __init__(self, books: Dict[int, time], location: int, max_weeks: int):
        self._books = books
        self._location = location
        self._timing = [0] * max_weeks

    def read(self, book: Book, start_time: int) -> Tuple[int, int]:
        """
            Reads book.
        :param book: Book -> book to be read.
        :param start_time: int -> start_time. The reading will start as
          soon as it can.
        :return [score, end_time] -> returns score to update the state and
            end time to update the book.
        """
        assert book.id_book in self._books, "Book not interested"
        assert (
            book._location == self._location
        ), f"Book is not in {self._location}, instead is in {book._location}"
        bdata = self._books[book.id_book]
        max_time = len(self._timing)
        for j in range(start_time, max_time):
            if self._timing[j] < 3:
                return self.__if_readable(bdata, book, j)
        return 0, start_time  # test it

    def __if_readable(self, bdata: time, book: Book, time: int) -> Tuple[int, int]:
        """
        if readable
        """
        max_time = len(self._timing)
        end_time = time + bdata
        score = 0 if end_time > max_time else book.score
        for j in range(time, min(end_time, max_time)):
            self._timing[j] += 1
        return score, end_time

    def __str__(self):
        return f"Book(books={self._books}, location={self._location}, _timing={self._timing})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (
            isinstance(other, Reader)
            and self._location == other._location
            and self._books == other._books
            and self._timing == other._timing
        )
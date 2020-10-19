#!/usr/bin/env python3
"""
State class declaration
"""
from typing import List, Dict, Tuple

from .book import Book
from .reader import Reader


class State:
    """
    State of the output line at the given line.
    """

    _transition: List[List[int]]
    _books: List[Book]
    _readers: List[Reader]
    _score: int

    def __init__(
        self,
        transition: List[List[int]],
        books: Dict[int, Book],
        readers: Dict[int, Reader],
    ):
        """
        Init does not parse file to avoid IO, so it is easy to test.
        """
        self._transition = transition
        self._books = books
        self._readers = readers
        self._score = 0

    def process_line(self, line: Tuple[int, str]) -> "State":
        """
        :param line : Tuple[int, str] where int is the number of the line,
        and str is the string to parse. It is provided the number of the line
        to show better errors in the messages.
        :return Either Exception State, where Exception
        is: line not correctly formated | state is not possible.
        """
        assert False, "not implemented"
        return self

    def __str__(self):
        return f"State(transition={self._transition}, books={self._books}, readers=self._readers, score={self.score})"

    def __repr__(self):
        return self.__str__()

#!/usr/bin/env python3
"""
Book class declaration
"""


class Book:
    """
    Represents the state of a book at a given time.
    """

    _location: int
    _internal_time: int
    id_book: int
    score: int

    def __init__(self, location: int, id_book: int, score: int):
        self._location = location
        self._internal_time = 0
        self.id_book = id_book
        self.score = score

    def move(self, location: int, time: int) -> None:
        """
        Moves book to a different location.
        :param location: int -> new location
        :param time: int -> time needed to move to the new
               location
        :return nothing, changes the current state of the book.
        """
        self._location = location
        self._internal_time += time

    def read(self, end_time: int) -> None:
        """
        The book is read for a period of time.
        :param time: int the period of time
        :return Nothing, changes the current state of the book.
        """
        assert (
            self._internal_time < end_time
        ), "Error, end of time is before the current state of the book"
        self._internal_time = end_time

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Reader(location={self._location}, internal_time={self._internal_time}, id_book={self.id_book})"

    def __eq__(self, other):
        return (
            isinstance(other, Book)
            and self._location == other._locationa
            and self._internal_time == other._internal_time
            and self.id_book == other.id_book
        )

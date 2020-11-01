from .Parser import Parser
from collections import namedtuple

"""
    namedtuple to store the library values that we read from the benchmark.
    @param id: id of the library
    @param time: array with the time that costs tranporting books from the
                 library to all others
"""
Library = namedtuple('Library', ['id', 'time'])

class LibraryParser(Parser):

    """
    Create a library from a line of the benchmark
    @param line: string with a line of the benchmark file
    """
    def parse(self, line):
        values = line.split()
        return Library(int(values[1]), [int(i) for i in values[2:]])

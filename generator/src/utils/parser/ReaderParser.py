from .Parser import Parser
from collections import namedtuple

"""
    namedtuple to store the reader values that we read from the benchmark.
    @param id: id of the reader
    @param id_library: id of the library the reader is suscribed
    @param books: array of tuples containing [(id_book, time_spent_reading)]
"""
Reader = namedtuple('Reader', ['id', 'id_library', 'books'])

class ReaderParser(Parser):

    """
    Create a reader from a line of the benchmark
    @param line: string with a line of the benchmark file
    """
    def parse(self, line):
        values = line.split()
        books_time = values[3:]
        books = []
        i = 0
        for i,value in enumerate(books_time):
            if i%2 == 0 and value != '\n':
                books.append((int(books_time[i]), int(books_time[i+1])))
        return Reader(int(values[1]), int(values[2]), books)

    
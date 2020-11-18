import random
import argparse
import sys
from collections import namedtuple
from .utils.checker.BookChecker import BookChecker
from .utils.checker.LibraryChecker import LibraryChecker
from .utils.checker.ReaderChecker import ReaderChecker
from .utils.checker.TimeChecker import TimeChecker
from .utils.parser.BookParser import BookParser
from .utils.parser.LibraryParser import LibraryParser
from .utils.parser.ReaderParser import ReaderParser
from .utils.parser.TimeParser import TimeParser

"""
    namedtuple to store the data related to books when creating
    the benchmark
    @param num: total number of books
    @param max_value: max value a book can provide when reading it
"""
BooksData = namedtuple("BooksData", ["num", "min_value", "max_value"])
"""
    namedtuple to store the data related to readers when creating
    the benchmark 
    @param num: total number of readers
    @param max_books: max number of books a reader can read
"""
ReaderData = namedtuple("ReaderData", ["num", "min_books", "max_books"])


class Generator:
    def __init__(self, num_of_libraries, bookdata, readerdata, filepath, time):
        self.num_of_libraries = num_of_libraries
        self.bookdata = bookdata
        self.readerdata = readerdata
        self.filepath = filepath
        self.output_file = open(self.filepath, "w")
        self.time = time
        self.getInstances = {
            "T": (
                TimeParser(),
                TimeChecker(
                    self.num_of_libraries, self.bookdata, self.readerdata, self.time
                ),
            ),
            "B": (
                BookParser(),
                BookChecker(
                    self.num_of_libraries, self.bookdata, self.readerdata, self.time
                ),
            ),
            "L": (
                LibraryParser(),
                LibraryChecker(
                    self.num_of_libraries, self.bookdata, self.readerdata, self.time
                ),
            ),
            "R": (
                ReaderParser(),
                ReaderChecker(
                    self.num_of_libraries, self.bookdata, self.readerdata, self.time
                ),
            ),
        }

    """
    Create and write in to the benchmark file all the libraries.
    """

    def create_libraries(self):
        max_transportation_time = self.time + 1
        for i in range(self.num_of_libraries):
            library_spec = "L " + str(i) + " "
            for j in range(self.num_of_libraries):
                if i == j:
                    library_spec += "0 "
                else:
                    library_spec += (
                        str(random.randint(1, max_transportation_time)) + " "
                    )
            library_spec += "\n"
            self.output_file.write(library_spec)

    """
    Create and write in to the benchmark file all the books.
    """

    def create_books(self):
        for i in range(self.bookdata.num):
            book_spec = (
                "B "
                + str(i)
                + " "
                + str(random.randint(self.bookdata.min_value, self.bookdata.max_value))
                + " "
                + str(random.randint(0, self.num_of_libraries - 1))
                + " "
            )
            book_spec += "\n"
            self.output_file.write(book_spec)

    """
    Create and write in to the benchmark file all the books.
    """

    def create_readers(self):
        assert (
            self.readerdata.max_books <= self.bookdata.num
        ), "Number of books that a reader can read must be lower than the total num of books!!"
        max_reading_time = self.time + 1
        for i in range(self.readerdata.num):
            reader_spec = (
                "R "
                + str(i)
                + " "
                + str(random.randint(0, self.num_of_libraries - 1))
                + " "
            )
            number_of_books_to_read = random.randint(
                self.readerdata.min_books, self.readerdata.max_books
            )
            books_set = random.sample(
                range(self.bookdata.num), k=number_of_books_to_read
            )
            for book in books_set:
                reader_spec += (
                    str(book) + " " + str(random.randint(1, max_reading_time)) + " "
                )
            reader_spec += "\n"
            self.output_file.write(reader_spec)

    """
    Create benchmark
    """

    def create(self):
        self.output_file.write("T " + str(self.time) + "\n")
        self.create_libraries()
        self.create_books()
        self.create_readers()

    """
    Check Values of the generated benchamark
    """

    def checkValues(self):
        generated_file = open(self.filepath, "r")
        for line in generated_file:
            print(line + "\n")
            parser, checker = self.getInstances[line[0]]
            elem = parser.parse(line)
            checker.check(elem)


def main():
    parser = argparse.ArgumentParser(description="Generates input file")
    parser.add_argument("max_time", type=int, help="Max time")
    parser.add_argument("num_books", type=int, help="Number of books")
    parser.add_argument("min_value_books", type=int, help="Minimum value of books")
    parser.add_argument("max_value_books", type=int, help="Maximum value of books")
    parser.add_argument("num_readers", type=int, help="Number of Readers")
    parser.add_argument(
        "min_books_reader", type=int, help="Minimum number of books to read"
    )
    parser.add_argument(
        "max_books_reader", type=int, help="Maximum number of books to read"
    )
    parser.add_argument("num_libraries", type=int, help="Number of libraries")
    parser.add_argument("benchmark", type=str, help="Benchmark output file")
    args = parser.parse_args()
    bookdata = BooksData(args.num_books, args.min_value_books, args.max_value_books)
    readerdata = ReaderData(
        args.num_readers, args.min_books_reader, args.max_books_reader
    )
    num_of_libraries = args.num_libraries
    time = args.max_time
    filepath = "benchmarks/" + args.benchmark
    generator = Generator(num_of_libraries, bookdata, readerdata, filepath, time)
    generator.create()
    generator.checkValues()


if __name__ == "__main__":
    main()

import random
import sys
from collections import namedtuple
from utils.checker.BookChecker import BookChecker
from utils.checker.LibraryChecker import LibraryChecker
from utils.checker.ReaderChecker import ReaderChecker
from utils.checker.TimeChecker import TimeChecker
from utils.parser.BookParser import BookParser
from utils.parser.LibraryParser import LibraryParser
from utils.parser.ReaderParser import ReaderParser
from utils.parser.TimeParser import TimeParser

"""
    namedtuple to store the data related to books when creating
    the benchmark
    @param num: total number of books
    @param max_value: max value a book can provide when reading it
"""
BooksData = namedtuple('BooksData', ['num', 'max_value'])
"""
    namedtuple to store the data related to readers when creating
    the benchmark 
    @param num: total number of readers
    @param max_books: max number of books a reader can read
"""
ReaderData = namedtuple('ReaderData', ['num', 'max_books'])


class Generator():

    def __init__(self, num_of_libraries, bookdata, readerdata, filepath, time):
        self.num_of_libraries = num_of_libraries
        self.bookdata = bookdata
        self.readerdata = readerdata
        self.filepath = filepath
        self.output_file = open(self.filepath, "w")
        self.time = time
        self. getInstances = {
            "T" : (TimeParser(), TimeChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)),
            "B" : (BookParser(), BookChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)),
            "L" : (LibraryParser(), LibraryChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time)),
            "R" : (ReaderParser(), ReaderChecker(self.num_of_libraries, self.bookdata, self.readerdata, self.time))
        }

    """
    Create and write in to the benchmark file all the libraries.
    @param num_of_libraries: Number of libraries to create
    @param output_file: File where to write the libraries
    @param time: Total time value to resolve the problem
    """

    def create_libraries(self):
        max_transportation_time = self.time + 1
        for i in range(self.num_of_libraries):
            library_spec = "L "+str(i)+" "
            for j in range(self.num_of_libraries):
                if i == j:
                    library_spec += "0 "
                else:
                    library_spec += (str(random.randint(1,max_transportation_time))+" ")
            library_spec += "\n"
            self.output_file.write(library_spec)

    """
    Create and write in to the benchmark file all the books.
    @param bookdata: namedtuple with the book creation specification values.
    @param output_file: File where to write the libraries
    @param num_of_libraries: Number of libraries to create
    """
    def create_books(self):
        for i in range(self.bookdata.num):
            book_spec = "B "+str(i)+" "+str(random.randint(1,self.bookdata.max_value))+" "+str(random.randint(0,self.num_of_libraries-1))+" "
            book_spec += "\n"
            self.output_file.write(book_spec)


    """
    Create and write in to the benchmark file all the books.
    @param readerdata: namedtuple with the reader creation specification values.
    @param bookdata: namedtuple with the book creation specification values.
    @param output_file: File where to write the libraries
    @param time: Total time value to resolve the problem
    @param num_of_libraries: Number of libraries to create
    """
    def create_readers(self):
        assert self.readerdata.max_books < self.bookdata.num, "Number of books that a reader can read must be lower than the total num of books!!"
        max_reading_time = self.time + 1
        for i in range(self.readerdata.num):
            reader_spec = "R "+str(i)+" "+str(random.randint(0, self.num_of_libraries-1))+" "
            number_of_books_to_read = random.randint(1,self.readerdata.max_books)
            books_set = random.sample(range(self.bookdata.num), k=number_of_books_to_read)
            for book in books_set:
                reader_spec += str(book)+" "+str(random.randint(1,max_reading_time))+" "
            reader_spec += "\n"
            self.output_file.write(reader_spec)

    def create(self):
        self.output_file.write("T "+str(self.time)+"\n")
        self.create_libraries()
        self.create_books()
        self.create_readers()


    def checkValues(self):
        generated_file = open(self.filepath, "r")
        for line in generated_file:
            print(line+"\n")
            parser, checker = self.getInstances[line[0]]
            elem = parser.parse(line)
            checker.check(elem)



def main():
    bookdata = BooksData(100000, 10)
    readerdata = ReaderData(1000, 10)
    num_of_libraries = 100
    time = 6
    if len(sys.argv) == 2:
        filepath = "benchmarks/"+sys.argv[1]
        generator = Generator(num_of_libraries, bookdata, readerdata, filepath, time)
        generator.create()
        generator.checkValues()
    else:
        print('Usage: python3 src/gen_input.py <filename>')  
        exit(-1)

if __name__ == "__main__":
    main()
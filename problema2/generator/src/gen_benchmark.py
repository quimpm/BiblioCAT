import random
import sys
from collections import namedtuple
from benchmark_checker import *

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

"""
Create and write in to the benchmark file all the libraries.
@param num_of_libraries: Number of libraries to create
@param output_file: File where to write the libraries
@param time: Total time value to resolve the problem
"""
def create_libraries(num_of_libraries, output_file, time):
    max_transportation_time = time + 1
    for i in range(num_of_libraries):
        library_spec = "L "+str(i)+" "
        for j in range(num_of_libraries):
            if i == j:
                library_spec += "0 "
            else:
                library_spec += (str(random.randint(1,max_transportation_time))+" ")
        library_spec += "\n"
        output_file.write(library_spec)

"""
Create and write in to the benchmark file all the books.
@param bookdata: namedtuple with the book creation specification values.
@param output_file: File where to write the libraries
@param num_of_libraries: Number of libraries to create
"""
def create_books(bookdata ,output_file, num_of_libraries):
    for i in range(bookdata.num):
        book_spec = "B "+str(i)+" "+str(random.randint(1,bookdata.max_value))+" "+str(random.randint(0,num_of_libraries-1))+" "
        book_spec += "\n"
        output_file.write(book_spec)


"""
Create and write in to the benchmark file all the books.
@param readerdata: namedtuple with the reader creation specification values.
@param bookdata: namedtuple with the book creation specification values.
@param output_file: File where to write the libraries
@param time: Total time value to resolve the problem
@param num_of_libraries: Number of libraries to create
"""
def create_readers(readerdata, bookdata, output_file, time, num_of_libraries):
    assert readerdata.max_books < bookdata.num, "Number of books that a reader can read must be lower than the total num of books!!"
    max_reading_time = time + 1
    for i in range(readerdata.num):
        reader_spec = "R "+str(i)+" "+str(random.randint(0, num_of_libraries-1))+" "
        number_of_books_to_read = random.randint(1,readerdata.max_books)
        books_set = random.sample(range(bookdata.num), k=number_of_books_to_read)
        for book in books_set:
            reader_spec += str(book)+" "+str(random.randint(1,max_reading_time))+" "
        reader_spec += "\n"
        output_file.write(reader_spec)

def create_file(num_of_libraries, bookdata, readerdata, file_name, time):
    output_file = open(file_name, "w")
    create_libraries(num_of_libraries, output_file, time)
    create_books(bookdata, output_file, num_of_libraries)
    create_readers(readerdata, bookdata, output_file, time, num_of_libraries)

def main():
    bookdata = BooksData(100000, 10)
    readerdata = ReaderData(1000, 10)
    num_of_libraries = 100
    time = 6
    if len(sys.argv) == 2:
        filepath = "benchmarks/"+sys.argv[1]
        create_file(num_of_libraries, bookdata, readerdata, filepath, time)
        checker = Checker(num_of_libraries, bookdata, readerdata, time)
        checkValues(checker, filepath)
    else:
        print('Usage: python3 src/gen_input.py <filename>')  
        exit(-1)

if __name__ == "__main__":
    main()
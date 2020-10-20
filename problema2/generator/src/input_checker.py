from .gen_input import *

class Book:
    def __init__(self, id_book, value, id_library):
        self.id_book = id_book
        self.value = value
        self.id_library = id_library

    def __eq__(self, book):
        return self.id_book == book.id_book and self.value == book.value and self.id_library == book.id_library

    def __str__(self):
        return "id_book: "+str(self.id_book)+", value: "+str(self.value)+", id_library: "+str(self.id_library)

class Library:
    def __init__(self, id_library, time):
        self.id_library = id_library
        self.time = time
        
    def __eq__(self, library):
        return self.id_library == library.id_library and self.time == library.time

    def __str__(self):
        return "id_library: "+str(self.id_library)+", time: "+str(self.time)

class Reader:
    def __init__(self, id_reader, id_library, books):
        self.id_reader = id_reader
        self.id_library = id_library
        self.books = books

    def __eq__(self, reader):
        return self.id_reader == reader.id_reader and self.id_reader == reader.id_reader and self.books == reader.books

    def __str__(self):
        return "id_reader: "+str(self.id_reader)+", id_library: "+str(id_library)+", books: "+str(self.books)

class Checker:
    def __init__(self, num_of_libraries, num_of_books, num_of_readers, max_book_value, time, max_num_books_reader_can_read):
        self.num_of_libraries = num_of_libraries
        self.num_of_books = num_of_books
        self.num_of_readers = num_of_readers
        self.max_book_value = max_book_value
        self.time = time
        self.max_num_books_reader_can_read = max_num_books_reader_can_read

    def checkBook(self, book):
        return (book.id_book >= 0 and book.id_book < self.num_of_books) and (book.value >= 1 and book.value <= self.max_book_value) and (book.id_library >= 0 and book.id_library < self.num_of_libraries) 

    def checkLibrary(self, library):
        if not((library.id_library >= 0 and library.id_library < self.num_of_libraries) and len(library.time) > 0):
            return False
        for i in library.time:
            if not(i >= 0 and i <= self.time+1):
                return False 
        return True
    
    def checkReader(self, reader):
        if not((reader.id_reader >= 0 and reader.id_reader < self.num_of_readers) and (reader.id_library >= 0 and reader.id_library < self.num_of_libraries) and (len(reader.books) >= 1 and len(reader.books) <= self.max_num_books_reader_can_read)):
            return False
        books_set = set()
        for i in reader.books:
            if not((i[0] >= 0 and i[0] < self.num_of_books) and i[0] not in books_set  and (i[1] >= 1 and i[1] <= self.time+1)):
                return False
            books_set.add(i)
        return True

def createBook(line):
    values = line.split()
    return Book(int(values[1]), int(values[2]), int(values[3]))

def createLibrary(line):
    values = line.split()
    return Library(int(values[1]), [int(i) for i in values[2:]])

def createReader(line):
    values = line.split()
    books_time = values[3:]
    books = []
    i = 0
    for i,value in enumerate(books_time):
        if i%2 == 0 and value != '\n':
            books.append((int(books_time[i]), int(books_time[i+1])))
    return Reader(int(values[1]), int(values[2]), books)

def checkValues(checker, filename):
    input_file = open(filename, "r")
    for line in input_file:
        print(str(line))
        if line[0] == "B":
            book = createBook(line)
            if not(checker.checkBook(book)):
                print("Error in Book: "+str(book.id_book))
                exit(-1)
        if line[0] == "L":
            library = createLibrary(line)
            if not(checker.checkLibrary(library)):
                print("Error in Library: "+str(library.id_library))
                exit(-1)
        if line[0] == "R":
            reader = createReader(line)
            if not(checker.checkReader(reader)):
                print("Error in Reader: "+str(reader.id_reader))
                exit(-1)
    print("All good baby")

def main():
    num_of_libraries = 100
    num_of_books = 100000
    num_of_readers = 1000
    max_book_value = 10
    time = 6
    filename = "input1.data"
    max_num_books_reader_can_read = 10
    create_file(num_of_libraries, num_of_books, num_of_readers, filename, max_book_value, time, max_num_books_reader_can_read)
    checker = Checker(num_of_libraries, num_of_books, num_of_readers, max_book_value, time, max_num_books_reader_can_read)
    checkValues(checker, filename)

if __name__=="__main__":
    main()
from .Checker import Checker

class BookChecker(Checker):

    def __init__(self, num_of_libraries, bookdata, readerdata, time):
        super(BookChecker, self).__init__(num_of_libraries, bookdata, readerdata, time)

    """
    Checks if the values of a book are correct
    @param book: Book namedtuple
    """
    def check(self, book):
        return (book.id >= 0 and book.id < self.bookdata.num) and (book.value >= 1 and book.value <= self.bookdata.max_value) and (book.id_library >= 0 and book.id_library < self.num_of_libraries) 

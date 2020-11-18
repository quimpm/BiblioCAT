from .Checker import Checker


class BookChecker(Checker):
    def __init__(self, num_of_libraries, bookdata, readerdata, time):
        super(BookChecker, self).__init__(num_of_libraries, bookdata, readerdata, time)

    """
    Checks if the values of a book are correct
    @param book: Book namedtuple
    """

    def check(self, book):
        return (
            (0 <= book.id < self.bookdata.num)
            and (self.bookdata.min_value <= book.value <= self.bookdata.max_value)
            and (0 <= book.id_library < self.num_of_libraries)
        )

from .Checker import Checker


class ReaderChecker(Checker):
    def __init__(self, num_of_libraries, bookdata, readerdata, time):
        super(ReaderChecker, self).__init__(
            num_of_libraries, bookdata, readerdata, time
        )

    def check(self, reader):
        """
        Checks if the values of a reader are correct
        @param reader: Reader namedtuple
        """
        if not (
            (0 <= reader.id < self.readerdata.num)
            and (0 <= reader.id_library < self.num_of_libraries)
            and (
                self.readerdata.min_books
                <= len(reader.books)
                <= self.readerdata.max_books
            )
        ):
            return False
        books_set = set()
        for i in reader.books:
            if not (
                (i[0] >= 0 and i[0] < self.bookdata.num)
                and i[0] not in books_set
                and (i[1] >= 1 and i[1] <= self.time + 1)
            ):
                return False
            books_set.add(i)
        return True

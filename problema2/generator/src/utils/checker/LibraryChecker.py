from .Checker import Checker

class LibraryChecker(Checker):

    def __init__(self, num_of_libraries, bookdata, readerdata, time):
        super(LibraryChecker, self).__init__(num_of_libraries, bookdata, readerdata, time)

    """
    Checks if the values of a Library are correct
    @param library: Library namedtuple
    """
    def check(self, library):
        if not((library.id >= 0 and library.id < self.num_of_libraries) and len(library.time) > 0):
            return False
        for i in library.time:
            if not(i >= 0 and i <= self.time+1):
                return False 
        return True
    
from .Checker import Checker

class TimeChecker(Checker):

    def __init__(self, num_of_libraries, bookdata, readerdata, time):
        super(TimeChecker, self).__init__(num_of_libraries, bookdata, readerdata, time)

    """
    Checks if the values of a reader are correct
    @param reader: Reader namedtuple
    """
    def check(self, time):
        return int(time) > 0
from abc import ABC

class Checker(ABC):
    
    def __init__(self, num_of_libraries, bookdata, readerdata, time):
        self.num_of_libraries = num_of_libraries
        self.bookdata = bookdata
        self.readerdata = readerdata
        self.time = time


    def check(self, elem):
        pass

    """
    Checks if the time value is valid
    """
    def checkTime(self):
        return self.time > 0
from .Parser import Parser

class TimeParser(Parser):

    """
    Creates a book from a line of the benchmark
    @param line: string with a line of the benchmark file
    """
    def parse(self, line):
        values = line.split()
        return int(values[1])
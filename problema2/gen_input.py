import random

def create_libraries(num_of_libraries, output_file, time):
    max_transportation_dist = time + 1
    for i in range(num_of_libraries):
        library_spec = "L "+str(i)+" "
        for j in range(num_of_libraries):
            if i == j:
                library_spec += "0 "
            else:
                library_spec += (str(random.randint(1,max_transportation_dist))+" ")
        library_spec += "\n"
        output_file.write(library_spec)

def create_books(num_of_books, max_book_value ,output_file):
    for i in range(num_of_books):
        book_spec = "B "+str(i)+" "+str(random.randint(1,max_book_value))
        book_spec += "\n"
        output_file.write(book_spec)

def create_readers(num_of_readers, output_file, num_of_books, time, max_num_books_reader_can_read):
    max_reading_time = time + 1
    for i in range(num_of_readers):
        reader_spec = "R "+str(i)+" "
        number_of_books_to_read = random.randint(1,max_num_books_reader_can_read)
        books = [ random.randint(1, num_of_books) for j in range(number_of_books_to_read)]
        for book in books:
            reader_spec += str(book)+" "+str(random.randint(1,max_reading_time))+" "
        reader_spec += "\n"
        output_file.write(reader_spec)


def create_file(num_of_libraries, num_of_books, num_of_readers, file_name, max_library_dist, max_book_value, time, max_num_books_reader_can_read):
    output_file = open(file_name, "w")
    create_libraries(num_of_libraries, output_file, time)
    create_books(num_of_books, max_book_value, output_file)
    create_readers(num_of_readers, output_file, num_of_books, time, max_num_books_reader_can_read)

def main():
    create_file(100, 100000, 1000, "input1.data", 316, 10, 6, 10)    

if __name__ == "__main__":
    main()
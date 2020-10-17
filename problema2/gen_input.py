import random
def create_libraries(num_of_libraries, max_dist, output_file):
    library_spec = "L "
    for i in range(num_of_libraries):
        library_spec += str(i)
        for j in range(num_of_libraries):
            if i == j:
                library_spec += "0 "
            else:
                library_spec += (str(random.randint(1,max_dist))+", ")
        output_file.write(library_spec)

def create_file(num_of_libraries, num_of_books, num_of_readers, file_name):
    output_file = open(file_name, "rw")
    create_librearies(num_of_libraries, 316, output_file)
    create_books(num_of_books, output_file)
    create_readers(num_of_readers, output_file)

def main():
    create_file(100, 100000, 1000, "input1.data")    

if __name__ == "__main__":
    main()
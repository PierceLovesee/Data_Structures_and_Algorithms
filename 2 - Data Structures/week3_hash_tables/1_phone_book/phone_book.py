#python3
#Pierce Lovesee
#February 26th, 2021

#Good job! (Max time used: 0.37/6.00, max memory used: 117358592/671088640.)

class Book:
    """ class of object that represents a phone Book
    supports the following functions:
    add - adds a name assotiated with a number to the phone book
    remove - deletes a name from the phone book assotiated with a given number
    find - returns the name assotiated with a given phone number """
    def __init__(self, N):
        self.book = ["not found"] * N

    def add(self, number, name):
        self.book[number] = name

    def remove(self, number):
        self.book[number] = "not found"

    def find(self, number):
        return self.book[number]

class Query:
    """ Class of objects representing individual queries to a phonebook
    eash object has up to three atributes:
    type - the type of query (find, remove, or add)
    number - the phone number associated with the query
    name - (only used in the add query) the given name to be associated with
            a given number"""
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    """ reads the 'n' queries into a list that is then pasted onto processing"""
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def process_queries(queries, N):
    """ Creates a Book object of size N to act as the phone book
    then processes each query"""
    book = Book(N)

    for query in queries:
        if query.type == 'add':
            book.add(query.number, query.name)

        if query.type == 'find':
            print(book.find(query.number))

        if query.type == 'del':
            book.remove(query.number)

if __name__ == "__main__":
    #total size of the phone book
    N = 10000007

    process_queries(read_queries(), N)

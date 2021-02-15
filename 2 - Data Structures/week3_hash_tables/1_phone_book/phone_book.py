# python3
# Pierce Lovesee
# Feb 14th, 2021

from math import floor
from itertools import repeat
N = 10000 # size of phone book

#class to track the type of input
class Query:
    def __init__(self, query):
        # stores the type of query (i.e. add, del, find)
        self.type = query[0]
        # stores the number in the query
        self.number = int(query[1])
        # assertion to make sure 7 digit number not starting w/ 0
        #assert self.number >= 1000000
        # stores name for add query
        if self.type == 'add':
            self.name = query[2]
            assert len(str(self.name)) < 16

def hashNumber(number):
    c = 0.347
    return floor(N * (number * c % 1))


def read_queries():
    n = int(input()) # first gets the number n of all queries expected
    # then runs a loop adding Query objects to the return list
    # each query is turned into a Query object by passing list generated by
    # split() to make Query object; loops n times
    # then passes the list of Query objects to process_queries
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    """ prints the responses in results list sent by the process_queries """
    print('\n'.join(result))

def process_queries(queries):
    """ processes the list of Query objects passed to it by the read_queries
    function"""

    result = []  # list of results from "find" queries
    contacts = dict(zip(range(N),repeat("not found"))) #hash table of contacts

    for query in queries:
        # process for 'add' query type
        # if we already have contact with such number,
        # we should rewrite contact's name
        if query.type == 'add':
            contacts[hashNumber(query.number)] = query.name

            # this portion used for cheking for collisions in has table
            # if contacts[hashNumber(query.number)] == "not found":
            #     contacts[hashNumber(query.number)] = query.name
            # else:
            #     contacts[hashNumber(query.number)] = (query.name + "collision or replacement")

        # find name associated with number, append name to results list
        # if the number does not have a name associated with it, appends
        # "not found"
        if query.type == 'find':
            result.append(contacts[hashNumber(query.number)])

        # if a contact is deleted, the name is reset to "not found" for number
        if query.type == 'del':
            contacts[hashNumber(query.number)] = "not found"

    # then passes results list to write_responses
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

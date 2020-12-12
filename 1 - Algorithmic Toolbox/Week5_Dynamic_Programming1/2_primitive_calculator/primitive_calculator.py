# Pierce Lovesee
# December 11th, 2020
# written in Python3; will not work in python2
# I beleive this is due to an update to floating point arithmatic errors

import sys

def optimal_sequence(n):
    # creating a blank list for storing the minimum operations
    minOps = [0] * (n + 1)

    # determine the min ops for each incremental value, starting with 2
    for i in range(2, n + 1):
        # create a list of the results from the available operatoins
        ops = [i/3, i/2, i - 1]

        #start with the minops at each value at an infinite value
        # (i.e a value that will never be reached)
        minOps[i] = n + 10

        # determine if each operation is a.) valid, and b.) minimal based
        # on subsequent incremental's minimum operations
        for op in ops:
            if op % 1 == 0: # this checks to see if the operation is valid
                # must cast op to an intiger to properly index
                numOps = minOps[int(op)] + 1
                if numOps < minOps[i]: # this picks the best operation
                    minOps[i] = numOps # and stores it in the minOps array


    sequence = [] # blank list for storing the sequence of optimal values
    while n > 1:
        sequence.append(n)
        operations = [n/3, n/2, n - 1] # defines results of available ops.
        previousOps = n**2 #initialize necisarry ops of n to infinite value
        for operation in operations: # determine the best operation
            #this checks that each operation is valid
            if (op % 1 == 0) and (minOps[int(operation)] == minOps[n] - 1):
                proposedOps = minOps[int(operation)]
                if proposedOps < previousOps: # find the minimum ops path
                    n = int(operation) # and assign n to min ops index value
    sequence.append(1) # add 1 to the end of the list to satisfy grader

    return reversed(sequence) #reverse the sequence to satisfy grader

input = sys.stdin.read()
n = int(input)
assert 1 <= n <= 10**6                  # assertion based on grader input
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)                # shows the minimum ops to get value
for x in sequence:                      # prints out the returned list
    print(x, end=" ")

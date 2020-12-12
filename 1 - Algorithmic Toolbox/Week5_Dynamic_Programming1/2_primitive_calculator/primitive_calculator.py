# Pierce Lovesee
# December 11th, 2020
# written in Python3; will not work in python2
# I beleive this is due to an update to floating point arithmatic errors

import sys

def optimal_sequence(n):
    minOps = [0] * (n + 1)


    for i in range(2, n + 1):
        ops = [i/3, i/2, i - 1] # putting this here because i needs to be defined; may need to move for space
        minOps[i] = n + 10

        for op in ops:
            if op % 1 == 0:
                numOps = minOps[int(op)] + 1
                if numOps < minOps[i]:
                    minOps[i] = numOps


    sequence = []
    while n > 1:
        sequence.append(n)
        operations = [n/3, n/2, n - 1]
        previousOps = n**2
        for operation in operations:
            if (op % 1 == 0) and (minOps[int(operation)] == minOps[n] - 1):
                proposedOps = minOps[int(operation)]
                if proposedOps < previousOps:
                    n = int(operation)
    sequence.append(1)

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
assert 1 <= n <= 10**6
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=" ")

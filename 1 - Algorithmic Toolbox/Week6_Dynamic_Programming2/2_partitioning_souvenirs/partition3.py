# Uses python3
import sys
import itertools

def partition3(A):
    # first determine if sum of elements in array is divisable by 3
    if sum(a) % 3 != 0:
        return 0

    p  = int(sum(a) / 3)
    n = len(A) + 1

    # indexing T[row][column]
    # row increments up to p
    # column indexes along A elements
    T = [[True] * n for _ in range(p + 1)]

    # set first column = False; except T[0][0]
    # T[0][0] being set to True is stating "True, 0 can be added into p"
    # The rest of the 0th column initialized to false, other wise, this will
    # not work; everything in the table would evaluate to True
    # the 0th row has to be initalized to all True to represent that any valid
    # combo of elements in A summing to p can have 0 added to it and 
    for i in range(1, p + 1):
        T[i][0] = False

    for row in range()




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

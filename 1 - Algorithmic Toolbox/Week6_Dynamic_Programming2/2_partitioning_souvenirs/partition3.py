# Uses python3
import sys
import itertools

def partition3(A):
    # first determine if sum of elements in array is divisable by 3
    if sum(A) % 3 != 0:
        return 0

    p  = int(sum(A) / 3)
    n = len(A) + 1

    # indexing T[row][column]
    # row increments up to p
    # column indexes along A elements
    # **** trying initalizing the array with False instead
    # T = [[True] * n for _ in range(p + 1)]
    T = [[False] * n for _ in range(p + 1)]

    # set first column = False; except T[0][0]
    # T[0][0] being set to True is stating "True, 0 can be added into p"
    # The rest of the 0th column initialized to false, other wise, this will
    # not work; everything in the table would evaluate to True
    # the 0th row has to be initalized to all True to represent that any valid
    # combo of elements in A summing to p can have 0 added to it and
    # # **** trying with array initalized to False
    # for i in range(1, p + 1):
    #     T[i][0] = False
    for i in range(n):
        T[0][i] = True

    for row in range(1, p + 1):
        for column in range(1, n):
            # initialize subject cell as skipping the column(i) element in A
            #T[row][column] = T[row][column - 1]

            # check to see if A[column - 1] can be added in to the sum based on
            # previous elements
            if row >= A[column - 1]:
                T[row][column] = ((T[row][column]) or
                                    (T[row - A[column - 1]][column - 1]))

    for i in range(p + 1):
        print(i)
        print(T[i])

    # if T[p][n -1]:
    #     return 1
    # else:
    #     return 0

    result = 0
    for foo in T[p]:
        if foo:
            result += 1
    if result >= 3:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    assert len(A) == n
    assert 1 <= n <= 20
#    for i in A:
#        assert 1 <= i <= 30
    print(partition3(A))

# Pierce Lovesee
# December 14th, 2020

import sys
import itertools

def partition3(A):
    # first determine if sum of elements in array is divisable by 3
    # if not, then no point in continuing further
    if sum(A) % 3 != 0:
        return 0

    # if partitioning is possible, then the sum of elements in each partition3
    # will be equal to p
    p  = int(sum(A) / 3)

    n = len(A) + 1

    # indexing T[row][column]
    # row increments up to p
    # column indexes along A elements
    # initalize n * p array to all false
    T = [[False] * n for _ in range(p + 1)]

    # Next, set entire first row to True
    # T[0] being set to True is stating "True, 0 can be added into p"
    # all other elements in the table are still set to False
    # the 0th row has to be initalized to all True to represent that any valid
    # combo of elements in A summing to p can have 0 added to it and
    # still be valid.
    for i in range(n):
        T[0][i] = True

    # iterate for rows 1 through (p-1); row 0 is not evaluated (initalized to
    # True); row p evaluated in later in seperate loop
    for row in range(1, p):
        # iterate through columns 1 through n - 1; first column not evaluated
        # conseptiually, the first column is adding a null element to the sum;
        # so it will always be False
        for column in range(1, n):
            # initialize subject cell as skipping the column(i) element in A
            # this conseptually means that at this incremental value leading up
            # to p, adding this element into the sum will get you at least to
            # that point in 0 to p
            T[row][column] = T[row][column - 1]

            # check to see if A[column - 1] can be added in to the sum based on
            # previous elements
            if row >= A[column - 1]:
                # check to see if the subject element in A can be added to the
                # sum to p
                T[row][column] = ((T[row][column]) or
                                    (T[row - A[column - 1]][column - 1]))

    # this is the loop to determine the the values in the last row of the table
    # We canot carry over (or skip an element) from the previous column
    # if we did, once we find one valid solution, all the subsequent cells in
    # the last row would evaluate to True. In the last row, only cells
    # corisponding to valid combinations, with the corispoinding element in A
    # as the last element, will evaluate to True
    for column in range(1, n):
        if p >= A[column - 1]:
            T[p][column] = T[p - A[column - 1]][column - 1]

    # check the last row for Trues, if there are 3 or more Trues, then
    # it is possible to divide the souviners into 3 partitinos equally
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
    print(partition3(A))

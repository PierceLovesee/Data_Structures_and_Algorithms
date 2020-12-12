# Pierce Lovesee
# December 12th, 2020
# Completed Solution to KnapSack
# Result: (Max time used: 0.65/10.00, max memory used: 32243712/536870912.)

import sys

def optimal_weight(capacity, w):
    """
    Inputs
    capacity: int, total capacity of the sack
    w: list, weights of each bar of gold

    Output
    int, weight that maximizes gold taken, but does not exceed capacity
    """
    columns = len(w) + 1
    rows = capacity + 1
    # define 2 dimm list to hold possible results
    # capacity in the y axis; available item weights in the x axis
    Value = [[None] * columns for _ in range(rows)]

    for row in range(rows): # populate first column with 0's
        Value[row][0] = 0 # i.e. if no loot can be taken, value = 0

    # Look at each available item, one at a time (columns across top) **
    for column in range(1, columns): # available items
        # ** populating each sub-section of the capacity with how much
        # weight can be held in that sub-section of the bag (rows going down)
        # based on the item being looked at
        for row in range(rows):      # sack capacity
            # start by skipping the item and then evaluating
            Value[row][column] = Value[row][column - 1]

            # 'row' index value equivalent to the sub-section of capacity
            # you are considering at any given time
            # so, if the item under consideration is able to in the subsection
            # of capacity being looked at, then  ***
            if row >= w[column - 1]:
                # *** the maximum value is taken from either the value already
                # stored, or the value in the index back the item's weight
                # and over 1 to the left plus the items weight
                Value[row][column] = max(Value[row][column],
                                    Value[row - w[column - 1]][column - 1] +
                                     w[column - 1])

    return Value[capacity][len(w)]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))

    # assertions based on grader constraints
    assert 1 <= W <= 10**4
    assert 1 <= n <= 300
    for i in w:
        assert 1 <= i <= 10**5

    print(optimal_weight(W, w))

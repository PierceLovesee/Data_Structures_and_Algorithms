#Pierce Lovesee
#December 12th, 2020
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

    for column in range(1, columns): # available items
        for row in range(rows):      # sack capacity
            # start by skipping the item and then evaluating
            Value[row][column] = Value[row][column - 1]

            # row index value equivalent to
            if row > w[column - 1]:
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

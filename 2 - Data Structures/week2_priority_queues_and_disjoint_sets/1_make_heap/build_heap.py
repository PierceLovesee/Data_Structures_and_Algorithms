# python3
# Pierce Lovesee
# January 5th, 2021
# Grader Output: (Max time used: 0.21/3.0, max memory used: 26038272/536870912.)


def swap(data, swaps, x, y):
    """ Two indicies in the data array
    Swaps the two values at the given idexes in inplace
    Record the indicies swapped in the swaps list
    """
    data[x], data[y] = data[y], data[x]
    swaps.append((x, y))

def parent(i):
    """ Returns index of parent for node i
    """
    return((i-1) // 2)

def leftChild(i):
    """ Returns index of left node for node i
    """
    return((2*i) + 1)

def rightChild(i):
    """ Returns index of right node for node i
    """
    return((2*i) + 2)

def siftDown(data, swaps, i):
    maxIndex = i
    if leftChild(i) < len(data):
        L = leftChild(i)
        if ((L <= len(data)) and (data[L] < data[maxIndex])):
            maxIndex = L
    if rightChild(i) < len(data):
        R = rightChild(i)
        if ((R <= len(data)) and (data[R] < data[maxIndex])):
            maxIndex = R
    if i != maxIndex:
        swap(data, swaps, i, maxIndex)
        siftDown(data, swaps, maxIndex)

def siftUp(i):
    while ((i > 0) and (data[parent(i)] > data[i])):
        swap(parent(i), i)
        i = parent(i)

def buildHeap(data):
    """Build a heap from 'data' inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = [] # list to store tuple values of swapped indecies

    size = len(data) - 1 # current size of heap; max index
    for i in range((size // 2), -1, -1): # working up from leafs
    # each leaf is a proper tree, so must start from bottom and work up
        siftDown(data, swaps, i) # sift down called for each
    return(swaps)



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = buildHeap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

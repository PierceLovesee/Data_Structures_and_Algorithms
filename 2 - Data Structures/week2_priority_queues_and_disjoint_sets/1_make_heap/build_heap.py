# python3
# Pierce Lovesee
# January 5th, 2021


def swap(x, y):
    """
    Two indicies in the data array
    Swaps the two values at the given idexes in inplace
    Record the Indicies swapped in the swaps list
    """
    data[x], data[y] = data[y], data[x]
    swaps.append((x, y))

def parent(i):
    return((i-1) // 2)

def leftChild(i):
    return((2*i) + 1)

def rightChild(i):
    return((2*i) + 2)

def siftDown(i):
    maxIndex = i
    L = leftChild(i)
    if ((L <= len(data)) and (data[L] < data[maxIndex])):
        maxIndex = L
    R = rightChild(i)
    if ((R <= len(data)) and (data[R] < data[maxIndex])):
        maxIndex = R
    if i != maxIndex:
        swap(i, maxIndex)
        siftDown(maxIndex)

def siftUp(i):
    while ((i > 0) and (data[parent(i)] > data[i])):
        swap(parent(i), i)
        i = parent(i)

def buildHeap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []

    size = len(data) - 1
    for i in range((size // 2), -1, -1):
        siftDown(i)
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

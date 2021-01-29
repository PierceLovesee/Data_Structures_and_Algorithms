# python3
# Pierce Lovesee
# January 11th, 2021

from collections import namedtuple

class Heap(object):
    def __init__(self):
        """ The heap object is initalized as an empty node list
        also initalize a list that records the swaps made in the
        heap between elements"""
        self.heap = []
        self.swaps = []

    def __str__(self):
        """ Prints out the heap as list"""
        return self.heap

    def extractMax(self):
        """ Extracts and returns the max (top) element of the heap """
        size = len(self.heap)
        result = self.heap[0]
        self.heap[0] = self.heap[self.size]
        size = size - 1
        siftdown(0)
        return result

    def parent(self, i):
        """ returns the index of the parent node of the node at index 'i' """
        return((i-1) // 2)

    def leftChild(self, i):
        """ returns the index of the left child of the node at index 'i' """
        return((2*i) + 1)

    def rightChild(self, i):
        """ returns the index of the right child of the node at index 'i' """
        return((2*i) + 2)

    def siftDown(self, i):
        """ sifts the ith element down in the heap """
        maxIndex = i
        if leftChild(i) < len(self.heap):
            L = leftChild(i)
            if ((L <= len(self.heap)) and (self.heap[L].timeAvailable
            < self.heap[maxIndex].timeAvailable)):
                maxIndex = L

            # account for proper org. index order in min-heap
            elif ((L <= len(self.heap)) and
            (self.heap[L].orgIndex < self.heap[maxIndex].orgIndex)):
                maxIndex = L
        if rightChild(i) < len(self.heap):
            R = rightChild(i)
            if ((R <= len(self.heap)) and (self.heap[R].timeAvailable
            < self.heap[maxIndex].timeAvailable)):
                maxIndex = R

            # account for proper org. index order in min-heap
            elif ((R <= len(self.heap)) and
            (self.heap[R].orgIndex < self.heap[maxIndex].orgIndex)):
                maxIndex = R
        if i != maxIndex:
            swap(i, maxIndex)
            siftDown(maxIndex)

    def siftUp(self, i):
        while (((i > 0) and (self.heap[parent(i)].timeAvailable > self.heap[i].timeAvailable))
        or ((self.heap[parent(i)].timeAvailable == self.heap[i].timeAvailable)
        and (self.heap[parent(i)].orgIndex > self.heap[i].orgIndex))):
            swap(parent(i), i)
            i = parent(i)

    def swap(self, x, y):
        """ swaps the elemnts at index x and y in the heap
        and records the indexes of the elements swapped"""
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
        self.swaps.append((x, y))

    def buildHeap(self, n_workers):
        """ Build a heap of Workers from 'data' """
        for i in range((n_workers - 1), -1, -1):
            worker = Workers(i)
            self.heap.append(worker)
            siftDown(i)


class Workers(Heap):
    def __init__(self, n):
        self.orgIndex = n
        self.timeAvailable = 0


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


# naive implementation O(n^2)
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

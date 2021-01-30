# python3
# Pierce Lovesee
# January 11th, 2021
# Grader Output:
# (Max time used: 3.65/12.00, max memory used: 189681664/536870912.)

class Heap(object):
    def __init__(self):
        """ The heap object is initalized as an empty node list
        also initalize a list that records the swaps made in the
        heap between elements"""
        self.heap = []
        self.jobs = []
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
        self.siftDown(0)
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
        if self.leftChild(i) < len(self.heap):
            L = self.leftChild(i)
            # check which is available first
            if (self.heap[L].timeAvailable == self.heap[maxIndex].timeAvailable):
                if (self.heap[L].orgIndex < self.heap[maxIndex].orgIndex):
                    maxIndex = L
            elif (self.heap[L].timeAvailable < self.heap[maxIndex].timeAvailable):
                maxIndex = L

        if self.rightChild(i) < len(self.heap):
            R = self.rightChild(i)
            # check which is available first
            if (self.heap[R].timeAvailable == self.heap[maxIndex].timeAvailable):
                if (self.heap[R].orgIndex < self.heap[maxIndex].orgIndex):
                    maxIndex = R
            elif (self.heap[R].timeAvailable < self.heap[maxIndex].timeAvailable):
                maxIndex = R

        if i != maxIndex:
            self.swap(i, maxIndex)
            self.siftDown(maxIndex)

    def siftUp(self, i):
        while (((i > 0) and (self.heap[self.parent(i)].timeAvailable > self.heap[i].timeAvailable))
        or ((self.heap[self.parent(i)].timeAvailable == self.heap[i].timeAvailable)
        and (self.heap[self.parent(i)].orgIndex > self.heap[i].orgIndex))):
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def swap(self, x, y):
        """ swaps the elemnts at index x and y in the heap
        and records the indexes of the elements swapped"""
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
        self.swaps.append((x, y))


    def buildHeap(self, n_workers):
        """ Build a heap of Workers from 'data' """
        for i in range(n_workers):
            self.heap.append(Workers(i))
        for j in range((n_workers - 1), -1, -1):
            self.siftDown(j)


class Workers(Heap):
    """ Class of objects stored within the heap to represent
    each processing stream and when it will be available """
    def __init__(self, n):
        self.orgIndex = n
        self.timeAvailable = 0

class AssignedJob(Heap):
    """ Class of objects used to record when each job is started
    used to output result """
    def __init__(self, orgIndex, timeAvailable):
        self.worker = orgIndex
        self.start = timeAvailable


def assign_jobs(n_workers, jobs):
    workerHeap = Heap()
    workerHeap.buildHeap(n_workers)
    # do the following while the jobs list is not empty
    while bool(jobs):
        job = jobs.pop(0)
        workerHeap.jobs.append(AssignedJob(workerHeap.heap[0].orgIndex, workerHeap.heap[0].timeAvailable))
        workerHeap.heap[0].timeAvailable += job
        workerHeap.siftDown(0)
    return workerHeap.jobs



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.start)


if __name__ == "__main__":
    main()

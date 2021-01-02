#python3
# Pierce Lovesee
# Janurary 2nd, 2021
# using implementation of random3 quick sort incase few eunique values
# implementation developed in Algorithmic Tool box courser (course 1 of
# this specializatoin)

import sys
from random import randint

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return(str(self.__stack))

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()

    def Max(self):
        assert(len(self.__stack))
        MaxStack = []
        for i in self.__stack:
            MaxStack.append(i)


        def partition3(array, left, right):
            pivot = array[left]
            lessThan = left
            i = left
            greaterThan = right

            while i <= greaterThan:
                if array[i] < pivot:
                    array[lessThan], array[i] = array[i], array[lessThan]
                    lessThan += 1
                    i += 1
                elif array[i] > pivot:
                    array[i], array[greaterThan] = array[greaterThan], array[i]
                    greaterThan -= 1
                else:
                    i += 1
            return lessThan, greaterThan


        def randomized_quick_sort(array, left, right):
            if left >= right:
                return
            k = randint(left, right)
            array[left], array[k] = array[k], array[left]
            lessThan, greaterThan = partition3(array, left, right)
            randomized_quick_sort(array, left, lessThan - 1)
            randomized_quick_sort(array, greaterThan + 1, right)

        randomized_quick_sort(MaxStack, 0, len(MaxStack) - 1)
        return(MaxStack[-1])


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        elif query[0] == "print":
            print(stack)
        else:
            assert(0)

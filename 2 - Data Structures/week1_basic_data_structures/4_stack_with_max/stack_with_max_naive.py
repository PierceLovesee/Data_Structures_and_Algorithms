#python3
# Pierce Lovesee
# Janurary 2nd, 2021
# using implementation of random3 quick sort incase few eunique values
# implementation developed in Algorithmic Tool box courser (course 1 of
# this specializatoin)

import sys
from random import randint

# def binary_search(keys, query):
#     assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
#     assert 1 <= len(keys) <= 3 * 10 ** 4
#
#     high = len(keys) - 1
#     low = 0
#
#     while low <= high:
#         mid = (low + ((high - low) // 2))
#         if query == keys[mid]:
#             return mid
#         elif query < keys[mid]:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1

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


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.MaxStack = []

    def __str__(self):
        return(str(self.__stack))

    def Push(self, a):
        self.__stack.append(a)
        if (not bool(self.MaxStack)) or (self.MaxStack[-1] <= a):
            self.MaxStack.append(a)
        else:
            self.MaxStack.append(a)
            randomized_quick_sort(self.MaxStack, 0, len(self.MaxStack) - 1)


    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1] == self.MaxStack[-1]:
            self.__stack.pop()
            self.MaxStack.pop()
        else:
            pop = self.__stack.pop()
            self.MaxStack.remove(pop)

    def Max(self):
        return(self.MaxStack[-1])


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

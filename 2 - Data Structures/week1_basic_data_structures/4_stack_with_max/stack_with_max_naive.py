#python3
# Pierce Lovesee
# Janurary 2nd, 2021

import sys
from random import randint


class StackWithMax():
    def __init__(self):
        self.__stack = []   # two stacks need to be maintained; one as stack
        self.MaxStack = []  # and one to keep track of how many elemts can
                            # be removed and have the current max stay the
                            # max of the stack

    def __str__(self):              # print definintion for StackWithMax
        return(str(self.__stack))   # object

    def Push(self, a):  # handles new items being pushed to the stack
        self.__stack.append(a)  # appends new item to end of stack
        # if the MaxStack is empty, or if new element is larger than current
        # max, then append to end of MaxStack list
        if (not bool(self.MaxStack)) or (self.MaxStack[-1] <= a):
            self.MaxStack.append(a)
        # otherwise, the last element of the MaxStack is appened again
        # conceptually this means that if there are say 5 copies of the
        # same max element in a row, then 5 elements can be popped from
        # the stack while maintaining the same max
        else:
            max = self.MaxStack[-1]
            self.MaxStack.append(max)


    def Pop(self):  # pops elements from both stacks
        assert(len(self.__stack))
        self.__stack.pop()
        # as elements are popped from the main stack, the current maximum
        # is tracked with the MaxStack stack.
        self.MaxStack.pop()

    def Max(self):  # returns the last element of MaxStack
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

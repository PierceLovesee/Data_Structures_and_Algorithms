# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        #all indexes of children and keys initalized to 0
        #during input, if a node does not have a child, the corrisoponding indexes
        #are set to -1 for logical testing
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        #user input is read into the above arrays
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, n): # In-Order: Left --> Node --> Right
    ## need to totally reevalute how you are attacking this problem.
    ## -1 does not exist int he key list, -1 is found in the child list (left & right)

        if self.left[n] == -1:
            print(self.key[n], end = ' ')
            return
        self.inOrder(self.left[n])
        print(self.key[n], end = ' ')
        self.inOrder(self.right[n])

    # def preOrder(self): # Pre-Order: Node --> Left --> Right
    #     if self.key == -1:
    #         return
    #     print(self.key, end = ' ')
    #     self.inOrder(self.left)
    #     self.inOrder(self.right)
    #
    #
    # def postOrder(self): # Post-Order: Left --> Right --> Node
    #     if self.key == -1:
    #         return
    #     self.postOrder(self.left)
    #     self.postOrder(self.right)
    #     print(self.key, end = ' ')


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    # tree.preOrder()
    # tree.postOrder()

threading.Thread(target=main).start()

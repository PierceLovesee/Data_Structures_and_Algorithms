# python3
# Pierce Lovesee
# May 15th, 2021
# Max time used: 0.78/6.00, max memory used: 116871168/536870912.

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        #memory alocated for structure by initalizing arrays of size n to zero,
        #3 arrays are created, one for the values at each node,  then two to
        #hold the index of each nodes left and right child.
        #if a node does not have a child, the corrisoponding indexes
        # are set to -1 for logical testing
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
        # base case: once n is -1 we know we have gone as far left as possible
        if n == -1:
            return # so end recursion and return to previous stack frame
        self.inOrder(self.left[n]) # call on left child until base case reached
        print(self.key[n], end = ' ') # visit node in 'previous' frame
        self.inOrder(self.right[n]) # call on right child

    def preOrder(self, n): # Pre-Order: Node --> Left --> Right
        # base case: once n is -1 we know we have gone as far left as possible
        if n == -1:
            return # so end recursion and return to previous stack frame
        print(self.key[n], end = ' ') # visit node along route going left
        self.preOrder(self.left[n]) # call on left child
        self.preOrder(self.right[n]) # call on right children


    def postOrder(self, n): # Post-Order: Left --> Right --> Node
        # base case: once n is -1 we know we have gone as far left as possible
        if n == -1:
            return # so end recursion and return to previous stack frame
        self.postOrder(self.left[n]) #first recursivly call on left sub-tree
        self.postOrder(self.right[n])#second recursivly call on right sub-tree
        print(self.key[n], end = ' ')#visit node after both children visited


def main():
    tree = TreeOrders() # creat an instance of a TreeOrders object
    tree.read() # read in the values and structure of the tree from user input
    tree.inOrder(0) # traverse the tree inorder begining with the root node
    print("") #create new line in output print
    tree.preOrder(0) # traverse the tree in preorder starting with the root node
    print("") # create new line in output print
    tree.postOrder(0) # traverse the tree in postorder starting with root node

threading.Thread(target=main).start()

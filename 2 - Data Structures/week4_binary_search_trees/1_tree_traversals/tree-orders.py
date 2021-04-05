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

  def inOrder(self):
    self.result = [] # list for holding the inOrder result
    self.stack = [] #stack to keep track of where you've been
    i = 0 # index of the tree's root node in the list

    while True:

        # Find the left most child in each subtree
        if i != -1:
            # if you have not ran into a left leaf yet, append the current
            # node's index to the stack of where you have been
            self.stack.append(i)
            # next, look at the current node's left child
            i = self.left[i]

        # once the left most child is found, work back through the stack
        # visiting the nodes, then checking right subtrees/children
        elif(self.stack): # will not execute if stack is empty
            # work through the stack visiting nodes in the order of travaersal
            i = self.stack.pop()

            # visit the node and append its value to the results list
            self.result.append(self.key[i])

            # at each node, we know we have visited its left subtree and visited
            # the node itself, so we now need to visit the right subtree/child
            i = self.right[i]

        # once the stack is empty and i == -1, we know we have completed the
        # traversal; break out of the loop.
        else:
            break

    # return the results list of the inOrder traversal
    return self.result

  def preOrder(self):
      self.result = [] # list for holding the preOrder result
      self.stack = [] #stack to keep track of where you've been
      i = 0 # index of the tree's root node in the list

      while True:

          if i != -1:

              self.result.append(self.key[i])
              self.stack.append(i)
              i = self.left[i]

          elif(self.stack):
              i = self.stack.pop()
              i = self.right[i]

          else:
              break

      return self.result

  def postOrder(self):
      self.result = []

      def recursivePostOrder(node):
          if node == None:
              return
          recursivePostOrder()

      recursivePostOrder(self.key[0])
      return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

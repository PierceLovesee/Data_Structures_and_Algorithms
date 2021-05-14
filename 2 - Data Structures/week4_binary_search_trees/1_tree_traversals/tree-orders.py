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

  def inOrder(self): # In-Order: Left --> Node --> Right
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

  def preOrder(self): # Pre-Order: Node --> Left --> Right
      self.result = [] # list for holding the preOrder result
      self.stack = [] #stack to note what nodes we have visited
      i = 0 # index of the tree's root node (initialize)

      while True: # repeat the following until all nodes are visited
          if i != -1: # if we have not reached a leaf (-1 child)
              self.result.append(self.key[i]) # add this node to the results
              self.stack.append(i) # note that we have visited this node
              i = self.left[i] # go to this node's left child
          # once we reach a leaf going left, it's time to visit the right nodes
          elif(self.stack): # until the stack is empty
              i = self.stack.pop() # look at the last node
              i = self.right[i] # go to it's right child
          else:
              break # otherwise, break out of the True loop

      return self.result # return the results of the preOrder traversal

  def postOrder(self): # Post-Order: Left --> Right --> Node
      self.result = [] # holds results of traversal
      self.leftStack = [] # holds nodes that we have gone left from
      self.rightStack = [] # holds nodes that we have gone right from
      i = 0 # index of the root node (initalize)

      while True:  # repeate until all nodes are visited
          # prefer to go left; if we have not reached a leaf (-1 children) and
          # the current node has not already been visited and exited going left
          if (i not in self.leftStack) and (i != -1):
              self.leftStack.append(i) # then add it to the leftStack
              i = self.left[i] # and go to it's left child

          # otherwise, do the following while there are still nodes on the leftStack
          elif(self.leftStack):
              # i = self.leftStack[-1] # peek at the last node of the leftStack
              i = self.leftStack.pop()
              if i in self.rightStack: # **if we have gone right from that node
                  # i = self.leftStack.pop() # then remove it from leftStack
                  self.result.append(self.key[i]) # add it to results
                  if(self.leftStack): # then if leftStack is not empty
                      # i = self.leftStack[-1] # look at the top of leftStack again
                      i = self.leftStack[-1]
                  else:
                      break # otherwise, break out of the True loop
              else:  # **if we have not gone right from that node
                  self.leftStack.append(i) # add that node to the rightStack
                  self.rightStack.append(i) # add that node to the rightStack
                  i = self.right[i] # and visit its right child
          else:
              break # if all else failes, break out of the loop

      return self.result # return the results of the postOrder traversal

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()

#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree, root, nodes):
    def inOrder(root): # recursively returns the inorder traversal of the tree
        nonlocal tree # accesses the functions global variable of the tree
        nonlocal resultsLeft # accesses the functions global results list
        nonlocal resultsRight
        nonlocal nodesVisited # acces truth table tracking visited nodes
        # base case: once root is -1, we have gone as far left as possible
        if root == -1:
            return # so end recursion and return to previous stack frame
        inOrder(tree[root][1]) # call on left child until base case reached
        nodesVisited[root] = True # flip truth table value for node to show visited
        if not nodesVisited[0]:
            resultsLeft.append(tree[root][0])
        if nodesVisited[0]:
            resultsRight.append(tree[root][0])
        inOrder(tree[root][2]) # call on right child until base case reached
    # global base case: if no nodes in the tree, then it is a correct BST
    if not bool(tree):
        return True
    resultsLeft = [] # record of inorder traversal of left tree w/o root node
    resultsRight = [] # record of inorder traversal of right tree with root node
    nodesVisited = [False] * nodes # Truth table to track visited nodes
    inOrder(root) # call to determine the inOrder traversal of the tree
    # then, loop through list to check if each node in the inorder traversal
    # was larger than it's previous node (definition of a BST)
    #print(resultsLeft)
    #print(resultsRight)
    if ((len(resultsLeft) == 0) and (len(resultsRight) == 1)):
        return True # base case for a BST with only a root node
    if ((len(resultsLeft) == 1) or (len(resultsRight) == 1)):
        for i in resultsRight:
            resultsLeft.append(i)
        for i in range(nodes - 1):
            if resultsLeft[i] > resultsLeft[i+1]: # if fails in any case, return False
                return False
    else:
        for i in range(len(resultsLeft) - 1):
            if resultsLeft[i] > resultsLeft[i+1]:
                return False
        if resultsLeft[-1] >= resultsRight[0]:
            return False
        for i in range(len(resultsRight) - 1):
            if resultsRight[i] > resultsRight[i+1]:
                return False

    return True # otherwise, the tree is a BST


def main():
  nodes = int(sys.stdin.readline().strip()) # total number of nodes
  tree = [] # blank list to store the nodes of the tree
  root = 0 # root of tree is set at 0th index
  # builds structure of tree as list of lists [[Val1, left1, right1], [Val2, ...
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree, root, nodes):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

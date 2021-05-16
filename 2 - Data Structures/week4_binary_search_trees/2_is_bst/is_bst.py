#python3
#Pierce Lovesee
#May 16th, 2021
#Good job! (Max time used: 0.40/10.00, max memory used: 157888512/536870912.)

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree, root, nodes):
    def inOrder(root): # recursively returs the inorder traversal of the tree
        nonlocal tree # accesses the functions global variable of the tree
        nonlocal results # accesses the functions global results list
        # base case: once root is -1, we have gone as far left as possible
        if root == -1:
            return # so end recursion and return to previous stack frame
        inOrder(tree[root][1]) # call on left child until base case reached
        results.append(tree[root][0]) # visit node in previous stack frame
        inOrder(tree[root][2]) # call on right child until base case reached
    # global base case: if no nodes in the tree, then it is a correct BST
    if not bool(tree):
        return True
    results = [] # blank list for recording the inorder traversal of the tree
    inOrder(root) # call to determine the inOrder traversal of the tree
    # then, loop through list to check if each node in the inorder traversal
    # was larger than it's previous node (definition of a BST)
    for i in range(nodes - 1):
        if results[i] > results[i+1]: # if fails in any case, return False
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

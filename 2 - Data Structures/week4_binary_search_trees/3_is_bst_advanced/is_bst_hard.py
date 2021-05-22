#python3
#Pierce Lovesee
#May 22nd, 2021
#Good job! (Max time used: 0.54/10.00, max memory used: 159129600/536870912.)

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree, root, nodes):
    def inOrder(root): # recursively returs the inorder traversal of the tree
        nonlocal tree # accesses the functions global variable of the tree
        nonlocal resultsInOrder # accesses the functions global resultsInOrder list
        # base case: once root is -1, we have gone as far left as possible
        if root == -1:
            return # so end recursion and return to previous stack frame
        inOrder(tree[root][1]) # call on left child until base case reached
        resultsInOrder.append(tree[root][0]) # visit node in previous stack frame
        inOrder(tree[root][2]) # call on right child until base case reached
    def preOrder(root): # recursively returns the preorder traversal of the tree
        nonlocal tree # accesses tree passed into parent function
        nonlocal resultsPreOrder # access resultsInOrder list for preorder traveral
        # base case: once root is -1, we have gone as far left/right as possible
        if root == -1:
            return
        # vist the node, record it's value to results, also record -1 to results
        # if current node has a right child, but no left child; this will be
        # crucial in testing correctness for duplicate value nodes.
        resultsPreOrder.append(tree[root][0])
        if ((tree[root][1] == -1) and (tree[root][2] != -1)):
            resultsPreOrder.append(-1)
        preOrder(tree[root][1]) # call on left child
        preOrder(tree[root][2]) # call on right child
    # global base case: if no nodes in the tree, then it is a correct BST
    if not bool(tree):
        return True
    resultsInOrder = [] # blank list for recording the inorder traversal
    resultsPreOrder = [] # blnk list for recording the preorder traversal
    inOrder(root) # call to determine the inOrder traversal of the tree
    preOrder(root) # call to determine the preorder traversal of the tree
    # then, check if each node in the inorder traversal
    # was larger than it's previous node (definition of a BST)
    for i in range(nodes - 1):
        if resultsInOrder[i] > resultsInOrder[i+1]: # if fails in any case, return False
            return False
    # then, check if any two consecutive nodes are equal in preorder traversal
    # if this is the case, then the tree is Incorrect; return False
    for i in range(len(resultsPreOrder) - 1):
        if resultsPreOrder[i] == resultsPreOrder[i+1]:
            return False

    return True # otherwise, the tree is a BST and duplicate nodes are only right children


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

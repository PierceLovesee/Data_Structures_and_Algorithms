# python3
# Pierce Lovesee
# December 27th, 2020
# Completed
# Grader Output:
# Good job! (Max time used: 1.07/3.00, max memory used: 163237888/536870912.)

import sys, threading

class Node(object):
    def __init__(self, parent, index, child = None):
        """
        Initialize a Node in the Tree
        Input:
            parent, index (title of node), child (default = None)
        Output:
            Creates new node with given parent, given title, and
            initailized with a child = None; child replaced later
            with a list of children nodes in AddChild funciton
        """
        self.parent = parent
        self.title = index
        self.children = child

    def __str__(self):
        return "This Node's Title: " + str(self.title) + "\nThis Node's Children: " + str(self.children) + "\n"

    def AddChild(self, childNode):
        """
        Adds a child node to a parent
        Input:
            childNode - The child node you wish to add to the given (self)
                        parent node.
        Output:
            Appends the childNode to the parent's child list (self.children)
        """
        if self.children == None:
            self.children = []
        self.children.append(childNode)


def treeHeight(node):
    """
    Determine Height of Tree
    Input:
        Node of a tree
    Output:
        Maximum height from root to leaves found in tree
    """
    # if there are no children to the node, then a leaf has been found,
    # no additional height past a leaf, return 0
    if node.children == None:
        return 0
    # initalize a list of depths at each node, with 0 prepopulated, to record
    # the height found down each child node path
    depths = [0]
    # iterate through all child nodes for given node, and determine it's Height
    # determined recursively
    for child in node.children:
        depths.append(treeHeight(child))
    # returns the max depth found plus 1 to account for path back to root
    return(1 + max(depths))



def main():
    n = int(input())
    parents = list(map(int, input().split()))

    #create list to store nodes
    nodeList = []
    # i is index location in parents list (title of node)
    # parent is value is parents list (parent of node)
    for i, parent in enumerate(parents):
        nodeList.append(Node(parent, i))

    # then look through the list of nodes; find root, and all other nodes added
    # them to their parent node
    for  i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            nodeList[parent].AddChild(nodeList[i])

    # check to make sure there is actually a tree:
    if len(nodeList) == 0:
        return 0

    #print out the max height found in the tree
    print(treeHeight(nodeList[root]) + 1)

    # exit program, no errors
    return 0



sys.setrecursionlimit(10**7) # increase max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()

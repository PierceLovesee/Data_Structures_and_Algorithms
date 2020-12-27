## Compute Tree Height on an Arbitrary (Can Be Non-Binary) Tree in Python3

### Problem Introduction:
Trees are used to manipulate hierarchical data such as hierarchy of categories of a retailer or the directory
structure on your computer. They are also used in data analysis and machine learning both for hierarchical clustering and building complex predictive models, including some of the best-performing in practice
algorithms like Gradient Boosting over Decision Trees and Random Forests.

The goal of this problem is to get used to trees. You will need to read a description of a tree from the input, implement the tree data structure, store the tree, and compute its height.

### Problem Description:
Given an input of a rooted non-binary or binary tree (arbitrary tree), compute the maximum height of the tree (max distance from root to furthest leaf).

**Input:** First prompt line will be ***n***, the number of nodes in the list.  Second prompt line will be the parent of each node seperated by spaces; the root node will have the parent ***-1***.  This input will be read into a list where the index of each element corisponds to the title of each node; the value at each index corisponds to the index, in the same list, of the subject node's parent node (i.e. list = [1, -1, 0]; node 0 has parent of node 1, node 1 is the root node, node 2 has parent of node 0).

**Output:** Prints a single integer representing the maximum height of the tree.

### Implementation:
The crux of this problem is to recognize that the trees given to the program will not necissarily be binary trees.  Therefore, the conventional structure for binary trees (i.e. left, right child nodes only; either or both may be Null) will not work in this application.  In order to handle this difference, each node will need a list in place of the child attribute.  So instead of considering ***node.child.left*** and ***node.child.right*** and being restricted to a finite number of children, we will consider a list of children for each node giving us an unlimited numer of children per node.  So, for example the ***c*** children in node ***Node1*** could be accessed as follows:

`Node1.children[0], Node1.children[1], ... , Node1.children[c - 1]`

Next we implement a class ***Node*** that allows us to populate a new list with ***Node*** objects, each having a ***parent*** attribute and a ***children*** (initalized to None) attribute.

Using this list of ***Node*** objects with the ***children*** atributes initailized to ***None***, we then go about finding the root of the tree and finding the children of each node.  Using the initial input list of ***Parents*** and the new list of ***Nodes*** we assign each node to it's respective parent node as an appended item to a newly formed list in the parent's ***children*** attribute.  If a node is found in inital list with a value equal to ***-1*** then that index is defined as the root of the tree.  This algorithm iterates through all elements of the two lists.  Once complete the node corrisponding to the root node will have all other nodes associated to it through each subsequent node's children list attribute.

In order to compute the maximum height of the tree, each node will need to return it's maximum height looking down towards its children.  With this naturally recursive problem, an eligent recursive solution evolves.  The base case for this recursive function is that if the children attribute of a node is equal to ***None*** then, by definition, that node is a leaf, and the max height below it is ***0***.  Other wise, or each node, we have to iterate through the node's list of children, computing each child node's height, adding 1 to it (to account for the distance between child and parent), storing that value in a list, and then once all of the child node heights have been computed, the maximum value is selected and returned.  This recursive solution is implemented is the ***treeHeight*** function. This function takes in a node as input, and recursively solves the height of each of the node's child nodes, returns the maximum, then adds ***1*** to account for the distance between the input node and its child node with maximum height.

Now, with a function that determines the height of a tree given an arbitrary node, and knowing the root of the tree, we pass the root node from the list of nodes (***nodeList[root]***) tot he ***treeHeight*** function and return the result.

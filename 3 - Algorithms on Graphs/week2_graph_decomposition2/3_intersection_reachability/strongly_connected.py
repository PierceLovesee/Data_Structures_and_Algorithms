#Uses python3
#Pierce Lovesee
#July 3, 2021
#Good job! (Max time used: 0.04/5.00, max memory used: 13611008/536870912.)

import sys

sys.setrecursionlimit(200000)

def toposort(adj, visitedNodes, inPath):
    """
    Takes as input an adjacency list of graph G, nodes visited truth table, and
    inPath truth table.  Returns a topological sorted traversal path of
    the graph G.
    """
    postOrdering = [] #empty list to track the postorder

    def explore(v): #DFS helper to explore adjacent verticies recursively
        if visitedNodes[v]: #if the node has been visited, don't explore it
            return
        if inPath[v]: #if node has been seen in path previously, end recursion
            return
        inPath[v] = True #mark the node as being in the curring path
        for i in adj[v]: #recursively explore all adjacent nodes
            explore(i)
        visitedNodes[v] = True #once all adjacent nodes explored, mark visited
        postOrdering.append(v) #add the visited node to the post ordering

    def DFS(): #DFS to explore all verticies in the graph
        for v in range(len(visitedNodes)):
            explore(v)

    DFS() #envoke the DFS recursion on the graph

    return(postOrdering) # return the postordering

def numSCC(adj, visitedNodes, postOrder_R, scc):
    """
    Takes as input the adjacency list of a graph G, visitedNodes truth table
    of G, the post-order traversal of G^R, and a list to track to which SCC each node
    belongs.
    Returns the total number of SCCs in G
    """

    if not bool(adj): #return 0 scc if adjacency list is empty
        return 0

    sccNum = 0 #if graph is non-empty, at least 1 SCC

    def explore(v): #DFS helper to explore adjacent verticies recursively
        nonlocal sccNum
        if visitedNodes[v]: #if the vertex has been visited, don't explore
            return
        if scc[v] == sccNum: #if vertex is in the current SCC, break recursion
            return
        scc[v] = sccNum #mark vertex as being in the current SCC
        for i in adj[v]:#recursively explore all adjacent verticies
            explore(i)
        #after adjacent verticies are explored, mark visited
        visitedNodes[v] = True

    def DFS(): #DFS implementation to determing num of SCC in graph
        nonlocal sccNum
        for count, v in enumerate(postOrder_R): #explore each vertex in graph
            if scc[v] == 0: #if vertex is already in a SCC, don't explore
                sccNum += 1 #increment the SCC
                explore(v)

    DFS() #envoke recursion on graph
    return sccNum # return the number of SCCs in the graph

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #create adjecency list for graph
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #create truth tables for visited nodes, SCCs, and tracking cycle paths
    visitedNodes = [False for _ in range(n)]
    scc = [0 for _ in range(n)]
    inPath = [False for _ in range(n)]
    #create adjacency list for reverse graph (G^R)
    adj_R = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_R[b - 1].append(a - 1)
    #find the postOrdering of the reverse graph (G^R)
    postOrdering_R = toposort(adj_R, visitedNodes, inPath)
    #reverse the list of the postordering of the reverse graph for easy use
    postOrder_R = []
    for _ in range(n):
        postOrder_R.append(postOrdering_R.pop())
    #reset the visited nodes truth table
    visitedNodes = [False for _ in range(n)]
    #determing the number of SCCs in the graph, display to user
    print(numSCC(adj, visitedNodes, postOrder_R, scc))

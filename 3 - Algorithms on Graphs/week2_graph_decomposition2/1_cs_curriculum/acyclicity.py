#python3
#Pierce Lovesee
#July 1, 2021
#Good job! (Max time used: 0.01/5.00, max memory used: 9416704/536870912.)

import sys

def acyclic(adj, visitedNodes, inPath):
    cycleExists = 0

    #DFS based helper function for exploring each path fully
    def explore(v):
        nonlocal cycleExists
        #base case if a cycle has already been found, stop further recursion
        if cycleExists == 1:
            return
        if visitedNodes[v]: #If a node has been visited, don't explore it
            return
        if inPath[v]: #If a node has been found in the path again, a cycle exists
            cycleExists = 1 #flip non-local variable to show a cycle exists
            return
        inPath[v] = True #otherwise, mark the node as being in the path
        for i in adj[v]: #then, recursively explore all adjacent verticies
            explore(i)
        # once all adjacent nodes are explored, mark verticy as Visited
        visitedNodes[v] = True

    def DFS():
        nonlocal cycleExists
        for v in range(len(visitedNodes)):
            explore(v)
        return cycleExists

    return(DFS())


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2] #n - num. vertices; m - num. edges (u to v with (w) weight)
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    visitedNodes = [False for _ in range(n)] #track nodes that are fully explored
    inPath = [False for _ in range(n)] #track what nodes are in a given path
    adj = [[] for _ in range(n)] #adjecency list
    for (a, b) in edges: # populate adjacency list
        adj[a - 1].append(b - 1) #populate adjacency list
    print(acyclic(adj, visitedNodes, inPath)) #print 1 for cyclic, 0 for acyclic

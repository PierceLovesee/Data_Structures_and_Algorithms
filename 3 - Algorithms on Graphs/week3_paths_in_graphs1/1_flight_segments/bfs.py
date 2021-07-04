#Uses python3
#Pierce Lovesee
#July 3rd, 2021

import sys
import queue

def distance(adj, s, t, dist, prev):
    """
    Input: adjacency list, start node int, target node int, distance list, and
    prev node list.

    Output: (int) the shortest distance between 's' and 't'
    """
    def BFS(): #helper function to perform breadth-first search on graph
        dist[s] = 0 #set start node's dist to zero
        Q = [s] #initialize queue with start node
        while bool(Q): #perform the following while Queue is not empty:
            u = Q.pop(0) #dequeue the next element, let it be 'u'
            for i in adj[u]: #for each adjacent node to 'u'
                if dist[i] == float('inf'): #if it has not been discovered
                    Q.append(i) #add it to the queue
                    dist[i] = dist[u] + 1 #set it's dist to dist[u] + 1
                    prev[i] = u #mark 'u' as its previous node
    BFS() #envoke the breadth first search on the graph
    if dist[t] == float('inf'): #if the target node was never discovered in BFS
        return -1 #return error since it cannot be reached from start node
    return dist[t] #otherwise, return the memoized distance to the target

def reconPath(s, t, prev):
    """
    Input: start node, target node, list of each node's previous shortest path
    node.

    Output: list of nodes to traverse the shortest path from start node to
    target node
    """
    if prev[t] ==  -1: #if a previous node was not recorded for the target
        #then return error message, no path from 's' to 't'
        return ("No Such Path Exists (" + str(s + 1) + ", " + str(t + 1) + ")")

    reconPathList = [] #list for storing the reconstructed path F/'t' T/'s'
    reversedPathList = [s + 1] #list for storing reversed path F/'s' T/'t'

    def constructPath(s, t): #helper function to reconstruct the path
        if t == s: #once 't' is 's', break recursion
            return
        reconPathList.append(t + 1) #add 't' to the path
        constructPath(s, prev[t]) #then recurs on 't's previous node

    def reversePath(): #helper to reverse the ordering of the list
        for _ in range(len(reconPathList)):
            reversedPathList.append(reconPathList.pop())

    constructPath(s, t) #reconstruct the path F/'s' T/'t'
    reversePath() #then reverse the path
    return(reversedPathList) #return the reversed path

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # Test Data Sets with Results Commented
    # data = [5, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 5] # -1
    # data = [4, 4, 1, 2, 4, 1, 2, 3, 3, 1, 2, 4] # 2
    # data = [5, 4, 5, 2, 4, 2, 3, 4, 1, 4, 4, 3] # 3
    n, m = data[0:2] #n - nodes | m - endges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2])) # list edges (u, v)
    adj = [[] for _ in range(n)] # undirected adjacency list
    for (a, b) in edges: #populate undrected adjacency list
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1 #s - source | t - target
    dist = [float('inf') for _ in range(n)] #initialize distance list to infinity
    prev = [-1 for _ in range(n)] #initialize prev. node array to -1 (no such node)
    print(distance(adj, s, t, dist, prev))
    #print(reconPath(s, t, prev)) # Uncommenting displays the node path

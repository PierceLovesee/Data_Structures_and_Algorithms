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
    def BFS():
        dist[s] = 0
        Q = [s]
        while bool(Q):
            u = Q.pop(0)
            for i in adj[u]:
                if dist[i] == float('inf'):
                    Q.append(i)
                    dist[i] = dist[u] + 1
                    prev[i] = u
    BFS()
    if dist[t] == float('inf'):
        return -1
    return dist[t]

def reconPath(s, t, prev):
    if prev[t] ==  -1:
        return ("No Such Path Exists (" + str(s + 1) + ", " + str(t + 1) + ")")

    reconPathList = []
    reversedPathList = [s + 1]

    def constructPath(s, t):
        if t == s:
            return
        reconPathList.append(t + 1)
        constructPath(s, prev[t])

    def reversePath():
        for _ in range(len(reconPathList)):
            reversedPathList.append(reconPathList.pop())

    constructPath(s, t)
    reversePath()
    # print("backwads path list", reconPathList)
    # print("forward path list", reversedPathList)
    return(reversedPathList)

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

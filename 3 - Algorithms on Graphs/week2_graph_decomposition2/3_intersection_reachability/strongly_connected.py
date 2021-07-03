#Uses python3
#Pierce Lovesee
#July 3, 2021

import sys

sys.setrecursionlimit(200000)

def toposort(adj, visitedNodes, inPath):

    postOrdering = []

    def explore(v):
        if visitedNodes[v]:
            return
        if inPath[v]:
            return
        inPath[v] = True
        for i in adj[v]:
            explore(i)
        visitedNodes[v] = True
        postOrdering.append(v)

    def DFS():
        for v in range(len(visitedNodes)):
            explore(v)

    DFS()

    return(postOrdering)

def numSCC(adj, visitedNodes, postOrder_R, scc):

    if not bool(adj): #return 0 scc if adjacency list is empty
        return 0

    sccNum = 1

    def explore(v):
        nonlocal sccNum
        if visitedNodes[v]:
            return
        if scc[v] == sccNum:
            return
        scc[v] = sccNum
        for i in adj[v]:
            explore(i)
        visitedNodes[v] = True


    # will need to be revisited
    def DFS():
        nonlocal sccNum
        for count, v in enumerate(postOrder_R):
            if scc[v] == 0:
                explore(v)
                if count < (len(postOrder_R) - 1):
                    sccNum += 1

    DFS()

    return sccNum

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [5, 7, 2, 1, 3, 2, 3, 1, 4, 3, 4 ,1, 5, 2, 5, 3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    #print(adj)
    visitedNodes = [False for _ in range(n)]
    scc = [0 for _ in range(n)]
    inPath = [False for _ in range(n)]

    adj_R = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_R[b - 1].append(a - 1)

    #print(adj_R)
    postOrdering_R = toposort(adj_R, visitedNodes, inPath)
    #print(postOrdering_R)
    postOrder_R = []
    for _ in range(n):
        postOrder_R.append(postOrdering_R.pop())
    visitedNodes = [False for _ in range(n)]

    print(numSCC(adj, visitedNodes, postOrder_R, scc))

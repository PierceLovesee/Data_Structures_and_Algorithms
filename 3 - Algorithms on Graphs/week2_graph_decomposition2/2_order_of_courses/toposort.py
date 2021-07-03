#Uses python3
#Pierce Lovesee
#July 2nd, 2021
#Good job! (Max time used: 0.27/10.00, max memory used: 39157760/536870912.)

import sys

def toposort(adj, visitedNodes):

    postOrdering = []  #keep track of the post ordering of the graph

    def explore(v):
        if visitedNodes[v]: #if the vertex has been visted, don't explore it
            return
        for i in adj[v]: #explore all adjacent verticies to 'v'
            explore(i)
        visitedNodes[v] = True #mark as visited when adjacent verticies explored
        postOrdering.append(v) #append vertex to post ordering record


    def DFS(): #perform DFS on graph to determine post ordering
        for v in range(len(visitedNodes)): #explore all verticies in the graph
            explore(v)
        return(postOrdering) #once complete, return te post ordering of graph

    return(DFS())

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visitedNodes = [False for _ in range(n)]
    order = toposort(adj, visitedNodes)
    for _ in range(n):
        print(order.pop() + 1, end=' ')

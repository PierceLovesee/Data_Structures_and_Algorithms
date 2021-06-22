#python3
#Pierce Lovesee
#June 19th, 2021

import sys

def reach(adj, x, y, nodeTruth):
    def explore(v, CC):
        nonlocal nodeTruth
        nodeTruth[(v)][0] = True #mark the node as visited
        nodeTruth[(v)][1] = CC #note what group of connected components
        for i in adj[v]: #for every connected node to v in the adj list
            if not nodeTruth[(i)][0]: #if that node has not been visited
                explore(i, CC) #then visit it; come on, really do it.

    def DFS():
        nonlocal nodeTruth
        CC = 1
        for v in range(len(nodeTruth)): #loop through all verticies in the graph
            if not nodeTruth[v][0]: #if the node has not been visited
                explore(v, CC) #call explore on it (recursive)
                #move to next cc group after all nodes connected to v are found
                #CC = connected components (groups of connected nodes)
                CC += 1

    # iteratively and recursively explore all verticies and edges
    DFS() #envoke the depth first search of the nodes

    #determine if 'x' & 'y' are in the same group of connected components
    if nodeTruth[x][1] == nodeTruth[y][1]:
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split())) #stores user input
    n, m = data[0:2] #stores 'n' verticies and 'm' edges at start of user input
    data = data[2:] #defines the graph data as all other use input
    #isolates the list of edges for later iteration
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:] #stores what points we check for connectivity
    adj = [[] for _ in range(n)] #creates a list of 'n' empty lists
    x, y = x - 1, y - 1 #converts to list index format
    #loop to create adjacency list representation of graph
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #passes the adjacency list, start, and end to determine connectivity
    nodeTruth = [[False, 0] for _ in range(n)] #[(is visited), (connectivity)]
    print(reach(adj, x, y, nodeTruth))

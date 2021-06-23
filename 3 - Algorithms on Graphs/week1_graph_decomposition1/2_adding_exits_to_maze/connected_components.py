#python3
#Pierce Lovesee
#June 22nd, 2021

import sys

def number_of_components(adj, nodeTruth):
    def explore(v, CC):
        nonlocal nodeTruth
        nodeTruth[(v)][0] = True #mark the node as visited
        nodeTruth[(v)][1] = CC #note what group of connected components
        for i in adj[v]: #for every connected node to v in the adj list
            if not nodeTruth[(i)][0]: #if that node has not been visited
                explore(i, CC) #then visit it; come on, really do it.

    def DFS():
        nonlocal nodeTruth
        CC = 0 # base case, empty graph would have zero components
        for v in range(len(nodeTruth)): #loop through all verticies in the graph
            if not nodeTruth[v][0]: #if the node has not been visited
                CC += 1
                explore(v, CC) #call explore on it (recursive)
                #move to next cc group after all nodes connected to v are found
                #CC = connected components (groups of connected nodes)
        return(CC)

    #iteratively and recursively explore all verticies and edges
    return(DFS())

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split())) #stores user input
    n, m = data[0:2] #stores 'n' verticies and 'm' edges at start of user input
    data = data[2:] #defines the graph data as all other use input
    #isolates the list of edges for later iteration
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)] #creates a list of 'n' empty lists
    #loop to create adjacency list representation of graph
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    nodeTruth = [[False, 0] for _ in range(n)] #[(is visited), (connectivity)]
    print(number_of_components(adj, nodeTruth))

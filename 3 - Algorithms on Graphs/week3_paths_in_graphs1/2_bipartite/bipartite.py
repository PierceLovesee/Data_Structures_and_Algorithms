#Uses python3
#Pierce Lovesee
#July 4th, 2020
#Good job! (Max time used: 0.25/10.00, max memory used: 45404160/536870912.)

import sys
import queue

#Note: not working fully.  failed grader test case.

def bipartite(adj):
    isBipartite = 1

    dist = [-1 for _ in range(len(adj))] #distance of each node from origin
    # Function to execute the breadth-first search
    def BFS(v):
        nonlocal isBipartite
        dist[v] = 0 #set the distance at the first node to 0
        Q = [v] # add the first node to the queue
        while bool(Q): #do the following while the queue is not empty
            if isBipartite != 1: #if non-bipartite node found; break the loop
                break
            u = Q.pop(0) #dequeue the next node in the queue, 'u'
            for i in adj[u]: #for each adjacent node to 'u'
                if dist[i] == -1: #if it has not been visited
                    Q.append(i) #add it to the queue
                    dist[i] = dist[u] + 1 #add set it's distance to dist[u] + 1
                else: #otherwise, if the node has been visited
                    #check if the two nodes belong to different Sets
                    #this is simply checking that only even level nodes are
                    #connected to odd level nodes, and visa-versa.
                    if ((dist[u] % 2) == (dist[i] % 2)):
                        isBipartite = 0 #if even is connected to even, or odd to
                        #odd, then return 0 signifying that the graph is not bipartite

    def islands(): #helper function to ensure that all islands are explored
        nonlocal isBipartite
        for v in range(len(adj)): #look at all verticies in the graph
            if isBipartite != 1: #if a non-bipartite node found; break the loop
                break
            if dist[v] == -1: #if the node has not been explored, perform BFS
                BFS(v)

    islands() #evoke the BFS of the different islands in the graph
    return(isBipartite) #return the result fo the BFS

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))

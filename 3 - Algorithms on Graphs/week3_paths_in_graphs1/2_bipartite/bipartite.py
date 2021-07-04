#Uses python3
#Pierce Lovesee
#July 4th, 2020

import sys
import queue

#Note: not working fully.  failed grader test case.

def bipartite(adj):
    dist = [-1 for _ in range(len(adj))] #distance of each node from origin
    # Function to execute the breadth-first search
    def BFS():
        dist[0] = 0 #set the distance at the first node to 0
        Q = [0] # add the first node to the queue
        while bool(Q): #do the following while the queue is not empty
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
                        return 0 #if even is connected to even, or odd to odd,
                        #then return 0 signifying that the graph is not bipartite
        return 1 #If the BFS executes succesfully, the graph is bipartite

    return(BFS()) #return the result fo the BFS

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

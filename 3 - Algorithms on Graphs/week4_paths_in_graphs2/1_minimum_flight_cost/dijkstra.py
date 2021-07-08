#Uses python3
#Pierce Lovesee
#July 6th, 2021
#Good job! (Max time used: 0.40/10.00, max memory used: 47517696/536870912.)

import sys
import queue

#Note: try using the min-heap, but inputing lists wtih the distance as the key.

def distance(adj, cost, s, t, dist, prev):

    def dijkstra(s): #implemendation of Dijkstra's algorithm
        Q = queue.PriorityQueue() #create instance of priority queue
        for i in range(len(dist) - 1): #initialize (n-1) distances to infinite
            Q.put([float('inf'), i]) #sort by distance, associate index
        Q.put([0, s]) # set distance to 's' to 0 in min-heap
        dist[s] = 0 # set distance in dist array to 0 for 's'
        while not Q.empty(): #while the queue is not empty, do the following:
             #sort Q by distace and save as the new array
            u = Q.get() #dequeue the node with the shortest distance from 's'
            if u[0] == float('inf'): #if 'u's distance from 's' is inf., break
                break
            # otherwise, do the following for all of 'u's adjacent nodes:
            for n, v in enumerate(adj[u[1]]):
                if dist[v] > dist[u[1]] + cost[u[1]][n]: #if a shorter path is found
                    dist[v] = dist[u[1]] + cost[u[1]][n] #save that path
                    Q.put([dist[v], v]) #and add that node to the min-heap
                    prev[v] = u[1]# record the previous node for the shortest path
    dijkstra(s) #envoke Dijkstra's algorithm
    tDist = dist[t] #determine the cost for 's' to 't'
    if tDist == float('inf'): #if 't' is unreachable from 's'
        return -1 #then return error
    return tDist #otherwise, return the cost-distance from 's' to 't'



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3] # 3
    # data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2] # -1
    # data = [5, 10, 3, 5, 49438153, 2, 3, 78072041, 3, 4, 12409612, 1, 3, 88526216, 5, 2, 6876525, 1, 4, 28703032, 4, 1, 24629785, 4, 5, 96300300, 4, 3, 317823, 2, 5, 22632987, 4, 2] #56632501
    # data = [5, 9, 1, 2, 4, 1, 3, 2, 2, 3, 2, 3, 2, 1, 2, 4, 2, 3, 5, 4, 5, 4, 1, 2, 5, 3, 3, 4 , 4, 1, 5] # 6
    n, m = data[0:2] #n - nodes | m - edges
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)] #adjacency list
    cost = [[] for _ in range(n)] #array for storing costs along paths
    for ((a, b), w) in edges: #populate adjacency list and cost array based on data
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1 #s - source node | t - target node
    dist = [float("inf") for _ in range(n)] #array to store distance from source
    prev = [-1 for _ in range(n)] #array for tracking previous node
    print(distance(adj, cost, s, t, dist, prev))

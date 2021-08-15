#Uses python3
#Pierce Lovesee
#July 8th, 2021
#Good job! (Max time used: 2.76/10.00, max memory used: 12136448/536870912.)

import sys

def negCycleDetect(adj, cost):
    dist = [1001 for _ in range(len(adj))] #set dist to 'large' value
    prev = [-1 for _ in range(len(adj))] #initial previous node to -1
    dist[0] = 0 #start with node #0, dist 0

    def relax(u, v, v_n): #relax function for optimizing path
        if dist[v] > dist[u] + cost[u][v_n]: #if a shorter path is found
            dist[v] = dist[u] + cost[u][v_n] #update the path
            prev[v] = u # and note the previous node

    def detectNegativeCycle(): #determine if a negative cycle exists
        distCycle1 = [] # blank list copying over dist list
        for i in range(len(adj)): #look at each element in the dist list
            distCycle1.append(dist[i]) # and then copy it to the new list
        #this time, only do the following once
        for u in range(len(adj)): #for each node
            for n, v in enumerate(adj[u]): #look at each node in adj list
                relax(u, v, n) #and relax it
                if dist[v] < distCycle1[v]: #if a shorter path is found at any point
                    return 1 #then a negative cycle has been found
        return 0 # otherwise, no negative cycle exists

    def Bellman_Ford(): #implementation of Bellman-Ford Algorithm
        for _ in range(len(adj)-1): # do the follwing N-1 times
            for u in range(len(adj)): #look at every node
                for n, v in enumerate(adj[u]): #and for all nodes in adj list
                    relax(u, v, n) #relax that node
        return(detectNegativeCycle()) #Then, see if neg. cycle exits


    return(Bellman_Ford()) #envoke Bellman-Ford Algorithm


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5] # 0
    # data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1] # 1
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negCycleDetect(adj, cost))

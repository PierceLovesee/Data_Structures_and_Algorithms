#Uses python3
#Pierce Lovesee
#July 6th, 2021

import sys
import queue


def distance(adj, cost, s, t, dist, prev):

    def dijkstra(s):
        Q = [[float('inf'), i] for i in range(len(adj))]
        Q[s][0] = 0
        dist[0] = 0
        while bool(Q):
            Q = sorted(Q)
            u = Q.pop(0)
            if u[0] == float('inf'):
                break
            for n, v in enumerate(adj[u[1]]):
                if dist[v] > dist[u[1]] + cost[u[1]][n]:
                    dist[v] = dist[u[1]] + cost[u[1]][n]
                    Q.append([dist[v], v])
                    prev[v] = u[1]
    dijkstra(s)
    tDist = dist[t]
    if tDist == float('inf'):
        return -1
    return tDist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5, 1, 3]
    # data = [3, 3, 1, 2, 7, 1, 3, 5, 2, 3, 2, 3, 2]
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
    dist = [float('inf') for _ in range(n)]
    prev = [-1 for _ in range(n)]
    print(distance(adj, cost, s, t, dist, prev))

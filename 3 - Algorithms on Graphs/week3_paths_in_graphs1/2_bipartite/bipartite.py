#Uses python3

import sys
import queue

def bipartite(adj):
    dist = [-1 for _ in range(len(adj))]

    def BFS():
        dist[0] = 0
        Q = [0]
        while bool(Q):
            u = Q.pop(0)
            for i in adj[u]:
                if dist[i] == -1:
                    Q.append(i)
                    dist[i] = dist[u] + 1
                else:
                    if ((dist[u] % 2) == (dist[i] % 2)):
                        return 0
        return 1
        
    return(BFS())

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

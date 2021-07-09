#Uses python3
#Pierce Lovesee
#July 8th, 2021

import sys

def negCycleDetect(adj, cost):
    dist = [float('inf') for _ in range(len(adj))]
    prev = [-1 for _ in range(len(adj))]
    dist[0] = 0

    def relax(u, v, v_n):
        if dist[v] > dist[u] + cost[u][v_n]:
            dist[v] = dist[u] + cost[u][v_n]
            prev[v] = u

    def detectNegativeCycle():
        distCycle1 = dist
        for u in range(len(adj)):
            for n, v in enumerate(adj[u]):
                relax(u, v, n)
                if dist[v] < distCycle1[v]:
                    return 1
        return 0

    def Bellman_Ford():
        for u in range(len(adj)):
            for n, v in enumerate(adj[u]):
                relax(u, v, n)
        return(detectNegativeCycle())


    return(Bellman_Ford())


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5] # 0
    data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1]
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

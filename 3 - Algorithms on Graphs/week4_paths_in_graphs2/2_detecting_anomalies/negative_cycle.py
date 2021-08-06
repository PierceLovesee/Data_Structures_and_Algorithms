#Uses python3
#Pierce Lovesee
#July 8th, 2021

import sys

def negCycleDetect(adj, cost):
    dist = [float('inf') for _ in range(len(adj))]
    prev = [-1 for _ in range(len(adj))]
    negCycleFound = 0

    def relax(u, v, v_n):
        if dist[v] > dist[u] + cost[u][v_n]:
            dist[v] = dist[u] + cost[u][v_n]
            prev[v] = u

    def detectNegativeCycle(start, passedQ):
        nonlocal negCycleFound
        distCycle1 = []
        for i in range(len(adj)):
            distCycle1.append(dist[i])
        while bool(passedQ):
            if negCycleFound == 1:
                break
            u = passedQ.pop(0)
            for n, v in enumerate(adj[u]):
                passedQ.append(v)
                relax(u, v, n)
                if dist[v] < distCycle1[v]:
                    negCycleFound = 1

    # this may be breaking the loop before all nodes are relaxed.
    # then it thinks a
    # may need to run DFS to find all reachable nodes first

    def Bellman_Ford(u):
        start = u
        Q = []
        Q.append(u)
        passedQ = []
        passedQ.append(u)
        while bool(Q):
            u = Q.pop(0)
            if negCycleFound == 1:
                break
            for n, v in enumerate(adj[u]):
                if v in passedQ:
                    break
                Q.append(v)
                passedQ.append(v)
                relax(u, v, n)
        detectNegativeCycle(start, passedQ)

    def disJointGraphs():
        for u in range(len(adj)):
            if negCycleFound == 1:
                break
            if dist[u] == float('inf'):
                dist[u] = 0
                Bellman_Ford(u)
        return negCycleFound

    return(disJointGraphs())


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = [4, 4, 1, 2, 1, 4, 1, 2, 2, 3, 2, 1, 3, 5] # 0
    # data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1] # 1
    # data = [10, 9, 1, 2, 1, 5, 6, 1, 6,  7, 1, 8, 9, 1, 9, 10, 1, 3, 4, 1, 7, 8, 1, 4, 5, 1, 2, 3, 1] # 0
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

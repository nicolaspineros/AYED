from sys import stdin
import heapq


def dijkstra(edges, s, t):
    n = len(edges)
    visited = [False for i in range(0, n)]
    d = [float('inf') for i in range(0, n)]
    q = []
    d[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        distance, u = heapq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in edges[u]:
                if (d[u] + w) < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(q, (d[v], v))
    return d[t]

def main():
    cases = int(stdin.readline())
    for c in range(cases):
        n, m, s, t = [int(x) for x in stdin.readline().split()]
        edges = [[] for x in range(n)]
        for i in range(0, m):
            u, v, w = [int(x) for x in stdin.readline().split()]
            edges[u].append((v, w))
            edges[v].append((u, w))
        ans = dijkstra(edges, s, t)
        if ans == float('inf'):
            print('Case #%d: unreachable' % (c + 1))
        else:
            print('Case #%d: %d' % (c + 1, ans))

main()

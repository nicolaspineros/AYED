from sys import stdin

def bellman_ford(edges, n, s, t):
    d = [float('inf') for i in range(0, n)]
    d[s] = 0
    for i in range(n - 1):
        for u, v, w in edges:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
    for u, v, w in edges:
        if d[u] + w < d[v]:
            return -1
    return d[t]

def main():
    cases = int(stdin.readline())
    for c in range(cases):
        n, m, s, t = [int(x) for x in stdin.readline().split()]
        edges = []
        for i in range(0, m):
            u, v, w = [int(x) for x in stdin.readline().split()]
            edges.append((u, v, w))
            edges.append((v, u, w))
        ans = bellman_ford(edges, n, s, t)
        if ans == float('inf'):
            print('Case #%d: unreachable' % (c + 1))
        else:
            print('Case #%d: %d' % (c + 1, ans))

main()

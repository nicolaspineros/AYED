from sys import stdin
import heapq

def dijkstra(edges, speeds, elevators_routes, s, t):
    visited = [False for i in range(0, 100)]
    d = [float('inf') for i in range(0, 100)]
    q = []
    d[s] = 0
    heapq.heappush(q, (0, -1, s))
    while q:
        distance, elevator, u = heapq.heappop(q)
        if not visited[u]:
            visited[u] = True
            if u == t:
                break
            for new_elevator in edges[u]:
                for v in elevators_routes[new_elevator]:
                    w = abs(v-u)*speeds[new_elevator]
                    if elevator != new_elevator and elevator != -1:
                        w += 60
                    if d[u] + w < d[v]:
                        d[v] = d[u] + w
                        heapq.heappush(q, (d[v], new_elevator, v))
    return d[t]

def main():
    while True:
        line = stdin.readline().strip()
        if line == '':
            break
        elevators, t = [int(x) for x in line.split()]
        speeds = [int(x) for x in stdin.readline().split()]
        edges = [[] for i in range(100)]
        elevators_routes = []
        for i in range(elevators):
            floors = [int(x) for x in stdin.readline().split()]
            for floor in floors:
                edges[floor].append(i)
            elevators_routes.append(floors)
        ans = dijkstra(edges, speeds, elevators_routes, 0 , t)
        if ans == float('inf'):
            print('IMPOSSIBLE')
        else:
            print('%d' % ans)

main()

from collections import deque
from sys import stdin
def bfs(L,V,n):
    global X
    pila = deque()
    pila.append(n)
    V[X.index(n)]=1
    M =[]
    while pila:
        u = pila.popleft()
        u = X.index(u)
        for v in L[u]:
            if(V[X.index(v)]==0):
                V[X.index(v)]=1
                pila.append(X[X.index(v)])
        M.append(u)
    return M
                
def main():
    global X
    L = []
    X = []
    n = int(stdin.readline().strip())
    for ZZ in range(n):
        """Aquí se llena el grafo L con los nodos y relaciones otorgadas  """
        line = str(stdin.readline().strip())
        a,b = line.split()
        a,b = int(a), int(b)
        if a not in X:
            X.append(a)
            L.append([])
        if b not in X:
            X.append(b)
            L.append([])
        A = X.index(a)
        B = X.index(b)
        if a not in L[B] or b not in L[A]:
            L[A].append(b)
            L[B].append(a)
    V=[0 for i in range(len(X))]
    M = []
    for i in range(len(L)):
        """ Se implementea el BFS con cada uno de los nodos que tienen al menos una conexión en el grafo. """
        H = len(bfs(L,V,X[i]))
        if H != 1:
            M.append(H)
    print(min(M), max(M))
main()

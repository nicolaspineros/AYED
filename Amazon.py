from sys import stdin
def distancia(l,p):
    D = []
    for i in l:
        if i == p:
            D.append(2<<31)
        else:
            d = (((i[0] - p[0]) ** 2) + ((i[1] - p[1]) ** 2)) ** (1/2)
            D.append(d)
    print( "Distancias:",D )
    for i in range(2):
        print( D.index( min( D ) ) )
        Grafo[p].append(l[D.index(min(D))])
        D[D.index(min(D))] = 2<<31
def BFS(visit,s):
    q = []
    q.append(s)
    visit[s] = True
    while q:
        s = q.pop()
        for i in Grafo[s]:
            if visit[i] == False:
                q.append(i)
                visit[i] = True
def main():
    global Grafo
    C = int(stdin.readline().strip())
    while C != 0:
        Grafo = dict()
        Visitados = dict()
        L = [int(i)for i in stdin.readline().strip().split()]
        I = 0
        U = []
        while True:
            if I == len(L):
                break
            U.append((L[I],L[I+1]))
            I += 2
        S = U[ 0 ]
        #print( U )
        U.sort()
        #print( U )
        for i in U:
            Grafo[i] = []
            Visitados[i] = False
        for i in U:
            distancia(U,i)
        BFS(Visitados,S)
        E = True
        for i in Visitados:
            if Visitados[i] == False:
                E = False
                break
        if E:
            print("All stations are reachable.")
        else:
            print("There are stations that are unreachable.")
        C = int(stdin.readline().strip())

main()

from sys import stdin
def BFS(s,v):
    for i in v:
        v[ i ] = False
    cont = 1
    q = [ s ]
    v[ s ] = True
    while q:
        u = q.pop( 0 )
        for i in Grafo[ u ]:
            if v[ i ] == False:
                q.append( i )
                v[ i ] = True
                cont += 1
    return cont
def main():
    global Grafo
    Cases = int( stdin.readline().strip() )
    for ZZ in range( Cases ):
        Grafo = dict()
        Visit = dict()
        I = int( stdin.readline().strip() )
        for i in range( I ):
            A,B = [ str( j ) for j in stdin.readline().strip().split() ]
            if A not in Grafo:
                Grafo [ A ] = []
                Visit [ A ] = False
            if B not in Grafo:
                Grafo [ B ] = []
                Visit [ B ] = False
            if B not in Grafo[ A ]: Grafo[ A ].append( B )
            if A not in Grafo[ B ]: Grafo[ B ].append( A )
            print( BFS( A,Visit ) )
main()

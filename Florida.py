from sys import stdin
def E(i,j):
    L = []
    for x in range( -1,2 ):
        for y in range( -1,2 ):
            if ( (i,j) != (i+x,j+y) ) and (M[i+x][j+y] == "W"):
                L += [( i+x,y+j )]
    G[(i,j)] = L
def BFS(s):
    VISIT = {}
    CONT = 0
    for i in G:
        VISIT [i] = False
    q = [s]
    while q:
        u = q.pop(0)
        for v in G[u]:
            if VISIT[v] == False:
                VISIT[v] = True
                CONT += 1
                q.append(v)
    return CONT
    
def main():
    global M,G
    cases = int( stdin.readline().strip() )
    blank = stdin.readline().strip()
    for ZZ in range( cases ):
        M = []
        C = []
        G = dict()
        D = str( stdin.readline().strip() )
        while D:
            if ( len( D.split() ) > 1 ):
                D = [int( i )  for i in D.split()]
                C.append( ( int( D[0] ),int( D[1] ) ) )
            else:
                S = [None]
                S += ( [str( i ) for i in D] )
                S += [None]
                M.append(S)
            D = str( stdin.readline().strip() )
        M.insert( 0, [None]*len( M[ 0 ] ) )
        M.append( [ None ] * len( M[ 0 ] ) )
        for i in range( len( M ) ):
            for j in range( len( M[0] ) ):
                if ( M[i][j] == "W" ):
                    E( i,j )
        for i in C:
            X = ( BFS( i ) )
            if X == 0:
                print( 1 )
            else:
                print( X )
        print()
main()


from sys import stdin
def E(i,j):
    D = []
    for x in range( -1,2 ):
        for y in range( -1,2 ):
            if ( abs( x ) != abs( y ) ):
                if L[i+x][j+y] != None:
                    D += [L[i+x][j+y]]
    G[L[i][j]] = D

def main():
    global L,G
    C = int( stdin.readline().strip() )
    for ZZ in range( C ):
        G = dict()
        W = dict()
        N = int( stdin.readline().strip() )
        M = int( stdin.readline().strip() )
        Lab = [[( i,j ) for i in range( M )] for j in range( N )]
        Lab.insert( 0,[ None for i in range( M + 2 ) ] )
        Lab.append( [ None for i in range( M + 2 ) ] )
        for i in Lab:
            if len( i ) == M:
                i.insert( 0,None )
                i.append( None )
            print( i )
        Weight = Lab.copy()
        print( Weight == Lab )
        
main()

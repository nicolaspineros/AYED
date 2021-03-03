from sys import stdin

class Set:
    
    def __init__( self ):
        self.p = self
        self.rank = 0
        
def FS( x ):
    if x.p != x:
        x.p = FS( x.p )
    return x.p

def Link( x,y ):
    Une( FS( x ),FS( y ) )
    
def Une( x,y ):
    if x.rank >= y.rank:
        y.p = x.p
        x.rank += 1
    else:
        x.p = y.p
        y.rank += 1
        
def K( L ):
    distance = 0
    Conjunto = Set()
    while W:
        X = min( W )
        if ( ( FS( CS[ L.index( X[ 1 ] ) ] ) ) ) != ( ( FS( CS[ L.index( X[ 2 ] ) ] ) ) ):
            Link( CS[ L.index( X[ 1 ] ) ],CS[ L.index( X[ 2 ] ) ] )
            distance += X[ 0 ]
        W.pop( W.index( X ) )
    print( "%.2f"%distance )
            
def distancia(l,p):
    for i in l:
        if i != p:
            d = (((i[0] - p[0]) ** 2) + ((i[1] - p[1]) ** 2)) ** (1/2)
            if ( ( d,p,i ) not in W ) and ( ( d,i,p ) not in W ):
                W.append( ( d,p,i ) )

def main():
    global W,CS
    C = int( stdin.readline().strip() )
    for ZZ in range( C ):
        G = dict()
        CS = []
        L = []
        stdin.readline().strip()
        P = int( stdin.readline().strip() )
        for c in range( P ):
            V = [ float( i ) for i in stdin.readline().strip().split() ]
            L.append( ( V[0],V[1] ) )
        W = []
        for i in L:
            CS.append( Set() )
            distancia( L,i )
        K( L )
        print()
main()

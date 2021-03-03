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
        
def Bellman( L ):
    distance = 0
    Conjunto = Set()
    while W:
#        print("W",W)
        X = min( W )
#       print("X",X)
#       print("CS",CS)
        if ( ( FS( CS[ L.index( X[ 1 ] ) ] ) ) ) != ( ( FS( CS[ L.index( X[ 2 ] ) ] ) ) ):
            Link( CS[ L.index( X[ 1 ] ) ],CS[ L.index( X[ 2 ] ) ] )
            distance += X[ 0 ]
        W.pop( W.index( X ) )
    print( "%.2f"%distance )            
def distancia(l,p):
    """ Generamos con base al grafo no dirigido un grafo no dirigido pero con pesos, guardando triplas de la forma (peso, coords ed a, coords ed b) """
    for i in l:
        if i != p:
            d = (((i[0] - p[0]) ** 2) + ((i[1] - p[1]) ** 2)) ** (1/2)
            if ( ( d,p,i ) not in W ) and ( ( d,i,p ) not in W ):
                W.append( ( d,p,i ) )

def main():
    global W,CS
    C = str( stdin.readline().strip() )
    while C != "":
        C = int(C)
        G = dict()
        CS = []
        L = []
        """ Generamos el grafo """
        for ZZ in range( C ):
            V = [ float( i ) for i in stdin.readline().strip().split() ]
            #print(V)
            L.append( ( V[0],V[1] ) )
        print(L)
        W = []
        CE = int(stdin.readline().strip())
        """ Creamos la lista de conjuntos necesarios para la implementacion de Bellman-Ford """
        for i in L:
            CS.append( Set() )
        for i in range(CE):
            a, b = [int(i) for i in stdin.readline().strip().split()]
            Link(CS[a-1],CS[b-1])
        for i in L:
            distancia( L,i )
        Bellman( L )
        C = str(stdin.readline().strip())
main()

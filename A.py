from sys import stdin

class Set:
    
    def __init__( self ):
        self.p = self
        self.rank = 1
        
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

def main():
    L = [i for i in stdin.readline().strip().split()]
    D = []
    ND = []
    for i in L:
        if i not in ND:
            ND.append(i)
            D.append(Set())
        else:
            D[ND.index(i)].rank += 1
    for i in range(len(ND)):
        print(ND[i], D[i].rank)
main()

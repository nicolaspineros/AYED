from sys import stdin
class C:
    def __init__(self,x):
        self.p = self
        self.rank = 0
def FindSet(x):
    if x.p != x:
        x.p = FindSet(x.p)
    return x.p
def Une(x,y):
    Link(FindSet(x),FindSet(y))
def Link(x,y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank = y.rank + 1
def main():
    global U
    ZZ = 1
    cases = [int(i) for i in stdin.readline().strip().split()]
    while cases != [0, 0]:
        U = [C(i) for i in range(cases[0]+1)]
        for I in range(cases[1]):
            A,B = stdin.readline().strip().split()
            A,B = int(A),int(B)
            Une(U[A],U[B])
        cont = 0
        for i in U[1:]:
            if i.p == i:
                cont += 1
        print("Case " + str(ZZ) + ": " + str(cont))
        ZZ += 1
        cases = [int(i) for i in stdin.readline().strip().split()]
main()

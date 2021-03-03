from sys import stdin
def suma(L,n):
    
    if len(L)==0 or n==0:
        sumi=0
    elif len(L)==n:
        sumi=sum(L)
    elif n==1:
        sumi=L[0]
    else:
        sumi=L[n-1]+suma(L,n-1)
    return sumi

def main():
    while True:
        L=[int(x) for x in stdin.readline().split()]
        valido=True
        while valido:
            n=int(stdin.readline().strip())
            if n>len(L):
                n=int(stdin.readline().strip())
            else:
                valido=False
        print(suma(L,n))
main()

'''
Casos Prueba:
INPUT:
1 2 3 4
3
OUTPUT:
6

INPUT:
1 2 3 4
0
OUTPUT:
0

INPUT:
1 2 3 4
100 (solicita nuevamente hasta que la entrada sea válida)
34
6
4
OUTPUT:
10

'''

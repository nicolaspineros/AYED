from sys import stdin
import sys
sys.setrecursionlimit(10000)
def muro(n):
    global memoria
    if memoria[n] is None:
        if n==1:
            res= 1
        elif n==2:
            res= 2
        else:
            res = muro(n-1) + muro(n-2)
        memoria[n] = res

    return memoria[n]

def main():
    global memoria
    num=int(stdin.readline())
    memoria = [None] * (300)
    while num!=0:

        print(muro(num))
        num=int(stdin.readline())
main()
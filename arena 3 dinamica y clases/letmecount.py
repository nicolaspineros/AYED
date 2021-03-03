from sys import stdin
import sys
sys.setrecursionlimit(30000)
def moneda(n,m):
    global monedas,memo
    if memo[m][n]==None:
        if m>4:return 0
        if n==0:
            return 1
        elif n<0:
            return 0
        memo[m][n]= moneda(n,m+1)+moneda(n-monedas[m],m)
    return memo[m][n]
def main():
    global monedas,memo
    a=int(stdin.readline())
    memo=[[None]*30001 for x in range(6)]
    monedas=[1,5,10,25,50]
    while a!=0:
        print(moneda(a,0))
        a=int(stdin.readline())
main()

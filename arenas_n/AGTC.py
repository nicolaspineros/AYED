from sys import stdin
import sys
sys.setrecursionlimit(100000)
def oper(i,j):
    global x,y,memo
    if memo[i][j] == None:
        if i==0 or j==0:
            res= i+j
        elif x[i] == y[j]:
            res= oper(i-1,j-1)
        else:
            res= 1+min(oper(i-1,j),oper(i,j-1),oper(i-1,j-1))
        memo[i][j] = res

    return memo[i][j]
def main():
    global x,y,memo
    while True:
        #Primera Linea
        y=[a for a in stdin.readline().split()]
        if not y:break
        m=int(y[0])
        y=[' ']+list(y[1])

        #Segunda Linea
        x=[a for a in stdin.readline().split()]
        n=int(x[0])
        x=[' ']+list(x[1])

        memo = [[None] * (m + 1) for x in range(n + 1)]
        #Hacer operaciones
        print(oper(n, m))


main()

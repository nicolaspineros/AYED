import time
from sys import stdin

def fibo(n):
    global memo

    if n not in memo:
        if n==1 or n==2:
            res= 1
        else:
            res= fibo(n-1)+fibo(n-2)
        memo[n]=res

    return memo[n]
            

def main():
    inicio=time.time()
    global memo
    memo={}
    n=int(stdin.readline().strip())
    print(fibo(n))
    print(memo)
    final=time.time()
    print(final-inicio)

main()


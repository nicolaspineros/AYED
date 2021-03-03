import time
import sys
import math
def threeNOneCycle(num):
    global memo
    if num not in memo:
     
        if num == 1:
            res= 1
        else:
            res= 1 + ( threeNOneCycle( ( num // 2 ) if ( num % 2 == 0 ) else ( 3*num+1) ) )
        memo[num]=res
        print(memo)
        
    return memo[num]
    
def threeNOne(n,m):
    maxN = -math.inf
    for i in range(n,m+1):
        maxN = max(maxN, threeNOneCycle(i))
    return maxN

def main():
    inicio=time.time()
    global memo
    memo={}
    line=sys.stdin.readline().strip()
    while line!='':
        n,m = [int(x) for x in line.split()]
        n,m = min(n,m),max(n,m)
        print(n,m,threeNOne(n,m))
        line=sys.stdin.readline().strip()
    fin=time.time()

    print(fin-inicio)
        

main()

import sys
import math
sys.setrecursionlimit(100000)
def main():
  casos=int(sys.stdin.readline().strip())
  for i in range(casos):
    N,W=sys.stdin.readline().strip().split()
    N=int(N)
    W=int(W)
    memo=[]
    for j in range(N+1):
      x=[]
      for h in range(W+1):
        x.append(None)
      memo.append(x)
    v=list(map(int,sys.stdin.readline().strip().split()))
    w=list(map(int,sys.stdin.readline().strip().split()))
    print(baul(N,W,w,v,0,memo))
def baul(N,W,w,v,vi,memo):
  if W<0:
    maxi= -math.inf   
    return maxi
  elif vi==N:
    return 0
  else:
    if memo[vi][W]==None:
      maxi=max(v[vi]+baul(N,W-w[vi],w,v,vi+1,memo),baul(N,W,w,v,vi+1,memo))
      memo[vi][W]= maxi
  return memo[vi][W]


main()

  

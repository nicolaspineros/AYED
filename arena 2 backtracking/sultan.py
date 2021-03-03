import sys
import math
global lis
def sultan(sp,ni,N,m,lis):
  if ni<N:
    for i in range(N):
      sp[ni]=i
      if valid(sp[:],ni):
        if ni < N-1:
          sultan(sp,ni+1,N,m,lis) 
        else:
          c=0
          for j in range(len(sp)):
            c+=m[sp[j]][j]
          lis.append(c)
          
          

def valid(sp,ni):
  isValid = True
  for x in range(0, ni):
    if sp[x] == sp[ni] or abs(sp[x] - sp[ni]) == abs(x - ni):
      isValid = False
      break
  return isValid
def solveNQueens(N,m,lis):
    sp, ni = [int(0) for x in range(0, N)], 0
    sultan(sp[:], ni, N,m,lis)
def main():
  a=int(sys.stdin.readline().strip())
  for j in range(a):
    N = 8
    m=[]
    for i in range(N):
      b=list(map(int,sys.stdin.readline().strip().split()))
      m.append(b)
    lis=[]
  #m=[[1, 2, 3, 4, 5, 6, 7, 8],[9, 10, 11, 12, 13, 14, 15, 16],[17, 18, 19, 20, 21, 22, 23, 24],[25, 26, 27, 28, 29, 30, 31, 32],[33, 34, 35, 36, 37, 38, 39, 40],[41, 42, 43, 44, 45, 46, 47, 48],[49, 50, 51, 52, 53, 54, 55, 56],[57, 58, 59, 60, 61, 62, 63, 64]]
    solveNQueens(N,m,lis)
    print(max(lis))

main()

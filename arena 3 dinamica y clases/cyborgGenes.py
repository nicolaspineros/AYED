from sys import stdin
"""def recursion(n,m):
  global a,b,dic,cont
  if memo[n][m]==None:
    if n==0 or m==0:
      memo[n][m] =n+m
    elif a[n]==b[m]:
      memo[n][m]= 1+recursion(n-1,m-1)
    else:
      memo[n][m] =1+min(recursion(n-1,m),recursion(n,m-1))
  return memo[n][m]"""
def main():
  global a,b,memo
  n=int(stdin.readline())
  for X in range(1,n+1):
    a=" "+stdin.readline().strip()
    b=" "+stdin.readline().strip()
    #memo=[[None]*len(b) for x in range(len(a))]
    #print(recursion(len(a)-1,len(b)-1))
    #for x in memo:print(x)
    n,m=len(a),len(b)
    memo=[[None]*m for x in range(n)]
    d=[[None]*m for x in range(n)]
    for i in range(n):
      memo[i][0]=i
      d[i][0]=1
    for j in range(m):
      memo[0][j]=j
      d[0][j]=1
    for i in range(1,n):
      for j in range(1,m):
        if a[i]==b[j]:
          memo[i][j]=1+memo[i-1][j-1]
          d[i][j]=d[i-1][j-1]
        else:
          memo[i][j]=1+min(memo[i-1][j],memo[i][j-1])
          if memo[i-1][j]==memo[i][j-1]:
              d[i][j]=d[i-1][j]+d[i][j-1]
          elif memo[i-1][j]<memo[i][j-1]:
              d[i][j]=d[i-1][j]
          else:
              d[i][j]=d[i][j-1]
        '''for x in memo:
          print(x)
        print("soy d XD")
        for y in d:
          print(y)
        print("--------------------------")'''
    print("Case #"+str(X)+":",memo[n-1][m-1],d[n-1][m-1])
main()

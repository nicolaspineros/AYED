import sys
def main():
  a = list(map(int,sys.stdin.readline().strip().split(',')))
  n = int(sys.stdin.readline().strip())
  print(sumlis(a,n))
def sumlis(a,n):
  b = a[n-1]+a[n]
  if n == 0:
    return a[0]
  a.insert(n-1,b)
  return sumlis(a,n-1)
  
main()

import sys
sys.setrecursionlimit(100000)
def main():
  global memo
  memo=[]
  a=sys.stdin.readline().strip()
  while a!="":
    a,b=[int(x)for x in a.strip().split()]
    z=[]
    print(a,b,lisnam(a,b,z))
    a=sys.stdin.readline().strip()
def lisnam(a,b,z):
  x=[]
  if a==b:
    z.append(enemas(b,x))
    return max(z)
  elif a > b:
    return lisnam(b,a,z)
  z.append(enemas(a,x))
  return lisnam(a+1,b,z)
def enemas(a,z):
  global memo
  if a==1:
    e=len(z)+1
    return e
  if a%2==0:
    b=a//2
    z.append(b)
    return enemas(b,z)
  else:
    c=3*a+1
    z.append(c)
    return enemas(c,z)
main()

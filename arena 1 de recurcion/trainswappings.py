import sys
def main():
  
  a=int(sys.stdin.readline().strip())
  for i in range(a):
    b=int(sys.stdin.readline().strip())
    c=list(map(int,sys.stdin.readline().strip().split()))
    if b != len(c):
      break
    print('Optimal train swapping takes',lista(c,0),'swaps.')
def lista(a,cont):
  b=min(a)
  d=a.index(b)
  if len(a)==1:
    return cont
  cont+=d
  a.pop(d)
  return lista(a,cont)
main()












































































































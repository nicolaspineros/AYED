import sys
def main():
  line=sys.stdin.readline().strip()
  while line!='':
    a,b=line.split()
    b=int(b)
    c=a*b
    print(sumsuper(c,[]))
    line=sys.stdin.readline().strip()
def sumsuper(c,lis):
  if len(c)==1:
    return c
  for i in range(len(c)):
    lis.append(int(c[i]))
  a=sum(lis)
  return sumsuper(str(a),[])
main()


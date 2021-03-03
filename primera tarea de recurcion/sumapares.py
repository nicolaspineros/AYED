import sys
def main():
  a=int(sys.stdin.readline().strip())
  print(sumapar(a))
def sumapar(a):
  b=a-2
  c=b+a
  if a==4 or a==2:
    return c
  elif a%2==1:
    return sumapar(a-1)
  d=sumapar(b-2)+c
  return d
main()

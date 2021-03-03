import sys
def main():
  a=sys.stdin.readline().strip().split(',')
  print(invertir(a))
def invertir(a):
  if len(a)==1:
    for i in range(len(a))
      a[i]=int(a[i])
      return a
  else:
    return [int(a[-1])]+invertir(a[:-1])
main()

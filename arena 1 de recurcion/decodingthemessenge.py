import sys
def main():
  a=int(sys.stdin.readline())
  c=input('')
  z=1
  for i in range(a):
    b=sys.stdin.readline().strip()
    print('')
    print('Case #'+str(z)+':')
    z=z+1
    while b!='':
      if ' 'not in b:
        print(b[0])
        b=sys.stdin.readline().strip()
      else:
        y=b[b.index(' ')+1:]
        print(''.join(repfil(y,2,[b[0]])))
        b=sys.stdin.readline().strip()
def repfil(a,b,z):
  g=a.split(' ')
  if len(g)==1:
    if len(g[0]) >= b:
      z.append(a[b-1])
      return z
    else:
      return z
  elif len(g[0]) >= b:
    z.append(a[b-1])
    a=a[a.index(' ')+1:]
    b=b+1
    return repfil(a,b,z)
  else:
    h=a[a.index(' ')+1:]
    return repfil(h,b,z)
      
    
main()

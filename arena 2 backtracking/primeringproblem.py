import sys
global c
def main():
  a=sys.stdin.readline()
  c=1
  while a!='': 
    a=int(a)
    b=[]
    for i in range(a):
      b.append(i+1)
    b.pop(0)
    print('case '+str(c)+':')
    back(a,0,b[:],[1])
    c+=1
    a=sys.stdin.readline()
def back(a,ai,b,sp):
  if ai < a:
    for i in range(len(b)):
      x=b[:]
      ele=x.pop(i)
      lisp = sp[:]
      lisp.append(ele)
      if valid(lisp[lisp.index(ele)-1]+ele):
        if ai < a-2:
          back(a,ai+1,x,lisp)
        else:
          if valid(lisp[0]+lisp[-1]):
            print(*lisp)
def valid(z):
    if z < 2:
      return False
    for i in range(2,z):
      if z%i==0:
        return False
      
    return True
main()
    

import sys
def main():
  w,L=list(map(int,sys.stdin.readline().strip().split()))
  while w!=0 and L!=0:
    u=[]
    for i in range(L):
      W,z=list(map(int,sys.stdin.readline().strip().split()))
      u.append((W,z))
    print(mochila(L,0,w,0,u[:],[],0))
    w,L=list(map(int,sys.stdin.readline().strip().split()))
def valid(wi,w):
  return wi <= w
def mochila(L,li,w,wi,u,sp,z):
  if L > li:
    maximochi=0
    for i in range(len(u)):
      lis=u[:]
      ele=lis.pop(i)
      spp=sp[:]
      spp.append(ele)
      if valid(ele[0]+wi,w):
        if li < L-1:
          maximochi=max(maximochi,z+ele[1],mochila(L,li+1,w,wi+ele[0],lis[:],spp[:],z+ele[1]))
        else:
          maximochi=max(maximochi,z+ele[1])
    return maximochi
main()
                        

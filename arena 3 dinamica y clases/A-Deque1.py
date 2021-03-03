import collections
import sys
class Lifoqueue(object):
  def __init__(self):
    self.data=collections.deque()
    self.head = None
  def pop(self):
    return self.data.pop()
  def agregar(self,value):
    return self.data.append(value)
  def añadir(self,value):
    return self.data.appendleft(value)
  def imprimir(self,value):
    return self.data[value]

lis= Lifoqueue()
queue=Lifoqueue()
a=int(sys.stdin.readline().strip())
while a!=0:
  n=a
  for i in range(a,0,-1):
      lis.agregar(i)
  while a!=1:
    queue.agregar(lis.pop())
    lis.añadir(lis.pop())
    a-=1
  print('Discarded cards:',end=' ')
  for i in range(n-2):
    print(queue.imprimir(i),end=', ')
  print(queue.imprimir(n-2))
  print('Remaining card:',lis.imprimir(0))
  for i in range(n-1):
    queue.pop() 
  lis.pop()
  a=int(sys.stdin.readline().strip())





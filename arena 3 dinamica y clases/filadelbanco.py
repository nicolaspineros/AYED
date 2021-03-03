import sys
class Nodo:
  def __init__(self,initdato):
    self.dato=initdato
    self.siguiente=None

  def obtenerDato(self):
    return self.dato
  def obtenerSiguiente(self):
    return self.siguiente
  def asignarDato(self,item):
    self.dato = item
  def asignarSiguiente(self,item):
    self.siguiente = item

class Banco:
  def __init__(self):
    self.cabeza=None
    self.cola=None
    self.len=0

  def agregar(self,item):
    item2=Nodo(item)
    if self.cola is None and self.cabeza is None:
      self.cabeza,self.cola=item2,item2
    else:
      self.cola.asignarSiguiente(item2)
      self.cola=item2
    self.len+=1
  def elifirst(self):
    valor=self.cabeza
    self.cabeza=valor.obtenerSiguiente()
    if self.cabeza is None:
      self.cola=None
    valor.asignarSiguiente(None)
    self.len-=1
    return valor.obtenerDato()
  def lenn(self):
    return self.len
  def printList(self):
    current = self.cabeza
    while current != None:
      if current.obtenerDato() is not None:
        print(current.obtenerDato())
        current = current.obtenerSiguiente()
  def firstele(self):
    valor=self.cabeza
    return valor.obtenerDato()

a=int(sys.stdin.readline().strip())
for i in range(a):
  b=int(sys.stdin.readline().strip())
  listo=Banco()
  for i in range(b):
    c=sys.stdin.readline().strip()
    if c=='Siguiente':
      if listo.lenn()==0:
        print('No hay fila')
      else:
        print(listo.elifirst())
        
    else:
      listo.agregar(c)
    

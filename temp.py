import hashlib
from sys import stdin

class hashtable(object):
  """implementa un diccionario con soporte para resolución de
  conflictos usando la ténica de 'chaining'"""

  """internamente la implementación utiliza una lista de Python como
  contenedor para los elementos y una variable entera que contabiliza
  la cantidad de elementos en el 'hashtable'"""
  __slots__ = '_table', '_n'

  def __init__(self):
    """un hashtable se crea vacio, con un contenedor que reserva 10000
    'buckets'"""
    self._table = list()
    self._n = 0
    hashtable._init_list(self._table, 10000)

  def _init_list(l, num):
    """agrega al final de 'l' tantos elementos 'None' como 'num'
    indica """
    for i in range(0, num):
      l.append([])

  def __str__(self):
    """calcula la representación de cadena de la tabla"""
    return " ".join([str(x) for x in self._table[0:self.n]])

  def _hash(self, key):
    """Calcula una funcion de hash para la llave"""
    raise ('Por Definir')
    m = hashlib.md5()
    m.update(str(key).encode('utf-8'))
    return int(m.hexdigest(), 16)

  def _compress(self, hcode):
    """Comprime el valor del hash a un bucket/slot valido en la tabla"""
    raise ('Por Definir')

  def put(self, k, v):
    """agrega la pareja (k, v)"""
    hash = self._init_list(v)
    if self._table[hash] is None:
      self._table[hash] = value

  def get(self, k):
    """obtener el valor asociado a k o None si no existe"""
    hash = self.Hash_func(v)
    if self._table[hash] is None:
      return None
    else:
      return hex(id(self.table[hash]))

  def delete(self,v):
    hash = self.Hash_func(v)
    if self._table[hash] is None:
        print("No Element found with value", v)
    else:
        print("Element with value", v, "deleted")
        self._table[hash] is None
        
H = hashtable()
H.put(0,"A")
H.put(1,"B")
H.put(2,"C")
print(H.get("A"))
print(H.get("B"))
print(H)

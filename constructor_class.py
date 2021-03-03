class complejo:

    nombre = "complejo"

    def __init__(self,real,imaginaria):
        self.r = real
        self.i = imaginaria

    def sumar(self,numero):
        self.r = self.r + numero.i
        self.r = self.i + numero.r

    def doble_sumar(self,numero)
        self.sumar(numero)
        self.sumar(numero)

    def __str__(self):
        return "(" + str(self.r) + "," + ")"

def suma_complejos(a,b):
    return (a.r + b.r , a.i + b.i)

a = complejo(3,5)
print(a)
print(a.r,a.i)
b = complejo(3,5)
print(b.r , b.i)
print(a == b)
"""nos da como resultado False ya que a pesar de tener los mismos atributos
tienen espacios distintos de almacenamiento"""
print(a.nombre)
print(b.nombre)
b.r = 1
print(a.r,a.i)
print(b.r , b.i)
a.sumar(b)
print(a.r,a.i)
a.doble_sumar(b)
print(a.r,a.i)
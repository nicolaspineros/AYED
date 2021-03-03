# Implementacion de un Heap minimal
from sys import stdin
import sys

class Heap: # Creamos la lase Heap

    def __init__(self):
        self.datos = [] # donde guardamos nuestra entrada para organizarla
        self.heap_size = 0

# establecemos los atributos de nuestro Heap que son el padre su parte izquierda y derecha
    def padre(self, i):
        return (i-1)//2

    def izquierda(self,i):
        return 2*i+1

    def derecha(self,i):
        return 2*i+2

    def min_heapify(self,i): # funcion para establecer el minimo
        I = self.izquierda(i)
        D = self.derecha(i)

        if I < self.heap_size and self.datos[I] < self.datos[i]:
            minimo = I

        else:
            minimo = i
        if D < self.heap_size and self.datos[D] < self.datos[minimo]:
            minimo = D

        if minimo != i:
            self.datos[i], self.datos[minimo] = self.datos[minimo], self.datos[i]
            self.min_heapify(minimo)

    def build_min_heap(self, A): # funcion para construir el heap
        self.heap_size = len(A)
        self.datos = A
        for i in range(len(A)//2, -1,-1):
            self.min_heapify(i)

    def min_heap_insert(self,key): # funcion de insercion
        self.heap_size = self.heap_size + 1
        self.datos.append(float("inf"))
        self.heap_decrease_key(self.heap_size - 1,key)
        #print(self.datos)

    def heap_decrease_key(self, i, key):
        self.datos[i] = key
        while i > 0 and self.datos[self.padre(i)] > self.datos[i]:
            self.datos[self.padre(i)], self.datos[i] = self.datos[i], self.datos[self.padre(i)]
            i = self.padre(i)

    def heap_extract_min(self): #funcion para extraer el minimo
        min = self.datos[0]
        self.datos[0] = self.datos[self.heap_size -1]
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return min

    def __str__(self):
        return " ".join([str(x) for x in self.datos[0:self.heap_size]])

def comprobacion(K,min_heap): #funcion para determinar la cantidad de pasos o si no es posible

    contador = 0
    while min_heap.heap_size > 1:
        #print("cantidad de elementos del heap: ",min_heap.heap_size)
        #print("Heap 1: ", min_heap)
        c1 = min_heap.heap_extract_min()
        c2 = min_heap.heap_extract_min()
        #print(c1)
        #print(c2)
        dulzura = c1 + 2 * c2   # Formula para determinar la dulzura
        #print("dulzura: ", dulzura)
        #print("Heap: ",min_heap)
        contador = contador + 1  # Determina el numero de operaciones
        if dulzura < K:
            min_heap.min_heap_insert(dulzura)
        else:
            break
    if dulzura > K:
        return contador
    else:
        return -1

def main():

    min_heap = Heap() #Creamos el Heap
    line=sys.stdin.readline().strip()
    N,K=line.split()
    N = int(N)
    K = int(K)
    cookie=list(map(int,stdin.readline().strip().split()))
    #print(cookie)
    for i in range(N):
        min_heap.min_heap_insert(cookie[i])
    #print(min_heap)
    resp = comprobacion(K,min_heap)
    print(resp)

    """
    
    #print("--- Prueba 1 ---")
    K = 7
    min_heap.min_heap_insert(1)
    min_heap.min_heap_insert(2)
    min_heap.min_heap_insert(3)
    min_heap.min_heap_insert(9)
    min_heap.min_heap_insert(10)
    min_heap.min_heap_insert(12)
    #print(min_heap)
    resp = comprobacion(K,min_heap)
    print(resp)
    
    """
    """

    print("--- Prueba 2 ---")
    K = 285
    min_heap.min_heap_insert(12)
    min_heap.min_heap_insert(1)
    min_heap.min_heap_insert(15)
    min_heap.min_heap_insert(20)
    print(min_heap)
    resp = comprobacion(K,min_heap)
    print(resp)

    """
main()

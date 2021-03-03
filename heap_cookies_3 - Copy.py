# Implementacion de un Heap minimal
from sys import stdin
import sys


class Heap:  # Creamos la lase Heap

    def __init__(self):
        self.datos = []  # donde guardamos nuestra entrada para organizarla
        self.heap_size = 0

    # establecemos los atributos de nuestro Heap que son el padre su parte izquierda y derecha
    def padre(self, i):
        return (i - 1) // 2

    def izquierda(self, i):
        return 2 * i + 1

    def derecha(self, i):
        return 2 * i + 2

    def min_heapify(self, i):  # funcion para establecer el minimo
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

    def build_min_heap(self, cookie):  # funcion para construir el heap
        self.heap_size = len(cookie)
        self.datos = cookie
        for i in range(len(cookie) // 2, -1, -1):
            self.min_heapify(i)

    def min_heap_insert(self, key):  # funcion de insercion
        self.heap_size = self.heap_size + 1
        self.datos.append(float("inf"))
        self.heap_decrease_key(self.heap_size - 1, key)

    def heap_decrease_key(self, i, key):
        self.datos[i] = key
        while i > 0 and self.datos[self.padre(i)] > self.datos[i]:
            self.datos[self.padre(i)], self.datos[i] = self.datos[i], self.datos[self.padre(i)]
            i = self.padre(i)

    def heap_extract_min(self):  # funcion para extraer el minimo
        min = self.datos[0]
        self.datos[0] = self.datos[self.heap_size - 1]
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return min

    def minimun(self):
        return self.datos[0]

    def __str__(self):
        return " ".join([str(x) for x in self.datos[0:self.heap_size]])



def main():

    min_heap = Heap()  # Creamos el Heap
    line = sys.stdin.readline().strip()
    while line !="":
        N, K = line.split()
        K = int(K)
        cookie = list(map(int, stdin.readline().strip().split()))
        # print(cookie)
        min_heap.build_min_heap(cookie)
        contador = 0
        while min_heap.minimun() < K:
            if min_heap.heap_size == 1:
                contador = -1
                break
            else:
                c1 = min_heap.heap_extract_min()
                c2 = min_heap.heap_extract_min()
                dulzura = c1 + (2 * c2)  # Formula para determinar la dulzura
                contador = contador + 1  # Determina el numero de operaciones
                min_heap.min_heap_insert(dulzura)
        print(contador)
        line = sys.stdin.readline().strip()

    """
    print("--- Prueba 1 ---")
    K = 7
    min_heap.min_heap_insert(1)
    min_heap.min_heap_insert(2)
    min_heap.min_heap_insert(3)
    min_heap.min_heap_insert(9)
    min_heap.min_heap_insert(10)
    min_heap.min_heap_insert(12)
    print(min_heap)
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
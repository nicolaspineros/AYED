# Implementacion de un Heap minimal

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

    def build_min_heap(self, A):
        self.heap_size = len(A)
        self.datos = A
        for i in range(len(A)//2, -1,-1):
            self.min_heapify(i)

    def min_heap_insert(self,key):
        self.heap_size = self.heap_size + 1
        self.datos.append(float("inf"))
        self.heap_decrease_key(self.heap_size - 1,key)
        #print(self.datos)

    def heap_decrease_key(self, i, key):
        self.datos[i] =key
        while i > 0 and self.datos[self.padre(i)] > self.datos[i]:
            self.datos[self.padre(i)], self.datos[i] = self.datos, self.datos[self.padre(i)]
            i = self.padre(i)

    def heap_extract_min(self):
        min = self.datos[0]
        self.datos[0] = self.datos[self.heap_size -1]
        self.heap_size = self.heap_size - 1
        self.min_heapify(0)
        return min

    def __str__(self):
        return " ".join([str(x) for x in self.datos[0:self.heap_size]])

def main():
    min_heap = Heap() #Creamos el Heap
    min_heap.min_heap_insert(33)
    min_heap.min_heap_insert(60)
    min_heap.min_heap_insert(5)
    min_heap.min_heap_insert(15)


    """while aux = 0:
        
        c1 = min_heap.heap_extract_min()
        c2 = min_heap.heap_extract_min()
        resp = c1 + 2*c2
        
        """

main()
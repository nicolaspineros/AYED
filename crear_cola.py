
class Cola: # Creamos la clase cola 
    def __init__(self):
        self.items = []

    def is_empty(self): # Metodo para verificar si la cola esta vacia
        return self.items == []

    def enqueue(self,item): # Metodo para agregar elementos a la cola
        self.items.append(item)

    def dequeue(self): # Metodo para eliminar el primer elemento en la cola
        self.items.pop(0)

    def print_cola(self): # Metodo para mostrar los elementos de la cola
        print(self.items)
        
cola = Cola() #creamos la cola

#Prueba

cola.enqueue("nico")
cola.enqueue(10)

cola.print_cola()

cola.dequeue()

cola.print_cola()        

# Recordar que la cola es de tipo FIFO (First In First Out)

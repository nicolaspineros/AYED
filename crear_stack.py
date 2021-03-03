
class Stack: #creamos la clase stack
    def __init__(self):
        self.items = []

    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []

    def push(self, item): # Metodo para insertar elementos a la pila
        self.items.append(item)

    def pop(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop()

    def print_stack(self): # Metodo para mostrar los elementos de la pila
        print(self.items)

pila = Stack() # Creamos la pila

# Prueba

pila.push("a")
pila.push("b")
pila.push("c")

pila.print_stack()


pila.pop()

pila.print_stack()

# Recordar que la pila es de tipo LIFO (Last In First Out)

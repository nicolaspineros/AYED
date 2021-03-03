# Cola con lista doblemente encadenada
# Nicolas Pileros Campo

class Node: # Creamos nuestra clase nodo que es la que vamos a usar como lista doblemente encadenada

    def __init__(self,key): # definimos nuestra llave y los apuntadores de la lista (next y prev)
        self.next = None
        self.prev = None
        self.key = key

    def __str__(self): # Metodo muestra del nodo y conversion
        return str(self.key)

class Cola: # Creamos la clase Cola 

    def __init__(self): # Construimos los atributos de la cola su head y tail
        self.head = None # cabeza
        self.tail = None # cola

    def enqueue(self,item): # Funcion para encolar o agregar elementos a la cola
        node = Node(item) # Generamos el nodo
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self): # Funcion para decolar o eliminar elementos a la cola o
        if self.head == None:
            raise Exception("Empty Stack") # excepcion cuando esta vacio
        node = self.head
        if node.next != None:
            node.next.prev = None
        self.head = node.next
        return node

    def __str__(self): # Metodo para mostrar la cola con solo los elementos
        cola = ''
        node = self.head
        while node != None:
            cola = str(node.key) + ' ' + cola
            node = node.next
        return cola

cola = Cola() # Creamos la cola

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola)
print(cola.dequeue())
print(cola)
        

from sys import stdin
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.prev = None
        self.next = None

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setPrev(self, newprev):
        self.prev = newprev

    def setNext(self, newnext):
        self.next = newnext

# Deque definition
class Mydeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueueFront(self,item):
        newnode = Node(item)
        if self.head == None and self.tail == None:
            self.head, self.tail = newnode, newnode
        else:
            #Asigna relacion
            newnode.setNext(self.head)

            if self.head is not None:
                self.head.setPrev(newnode)
            #Asigna el frente
            self.head = newnode

        self.len+=1

    def enqueueBack(self,item):
        newnode = Node(item)
        if self.head == None and self.tail == None:
            self.head, self.tail = newnode, newnode
        else:
            #Asigna relacion
            self.tail.setNext(newnode)
            newnode.setPrev(self.tail)
            #Asigna la cola
            self.tail = newnode

        self.len+=1

    def dequeueFront(self):
        newnode = self.head
        #Toma el siguiente como la nueva Cabeza
        self.head = newnode.getNext()
        #Eliminar relacion innecesaria
        newnode.setNext(None)

        if self.head is not None:
            self.head.setPrev(None)

        self.len -= 1

    def dequeueBack(self):
        if self.len == 0:
            return
        else:
            prenode = self.tail
            self.tail = prenode.getPrev()
            self.tail.setNext(None)

            self.len -=1

    def peekFront(self):
        return self.head.getData()

    def peekBack(self):
        return self.tail.getData()

    def printList(self):
        newnode = self.head
        while newnode != None:
            if newnode.getData() is not None:
                if newnode.getNext() is not None:
                    print('('+str(newnode.getData())+')',end='<-->')
                else:
                    print('('+str(newnode.getData())+')')


            newnode = newnode.getNext()

        if self.head is None:
            print ('Esta vacia')

deque = Mydeque()
n=int(stdin.readline().strip())
#Ingresar elementos a la fila
for i in range(n):
    deque.enqueueBack(i+1)
print('Lista con insercion interna')
deque.printList()
print()
print('Lista con insercion en frente')
deque.enqueueFront(10)
deque.printList()
print()
print('Lista con insercion atras')
deque.enqueueBack(11)
deque.printList()
print()
#Remover elementos a la fila
print('Despues de remover en frente')
deque.dequeueFront()
deque.printList()
print()
print('Despues de remover atras')
deque.dequeueBack()
deque.printList()
print()
print('Despues de remover en frente')
deque.dequeueFront()
deque.printList()
print()
print('Despues de remover atras')
deque.dequeueBack()
deque.printList()
print()
print('Despues de remover en frente')
deque.dequeueFront()
deque.printList()
print()
print('Despues de remover atras')
deque.dequeueBack()
deque.printList()

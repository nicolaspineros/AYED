from sys import stdin
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

# Queue definition
class Myqueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enqueue(self,item):
        newnode = Node(item)
        if self.head == None and self.tail == None:
            self.head, self.tail = newnode, newnode
        else:
            #Asigna relacion
            self.tail.setNext(newnode)
            #Asigna la cola
            self.tail = newnode
        self.len+=1

    def dequeue(self):
        newnode = self.head
        #Toma el siguiente como la nueva Cabeza
        self.head = newnode.getNext()
        #Eliminar relacion innecesaria
        if self.head is None:
            self.tail = None

        newnode.setNext(None)
        self.len-= 1

        return newnode

    def peek(self):
        return self.head.getData()

    def getLen(self):
        return self.len

    def printList(self):
        newnode = self.head
        while newnode != None:
            if newnode.getNext() is not None:
                print('(' + str(newnode.getData()) + ')', end='-->')
            else:
                print('(' + str(newnode.getData()) + ')')

            newnode = newnode.getNext()

        if self.head is None:
            print('Esta vacia')

queue = Myqueue()
n=int(stdin.readline().strip())
#Ingresar elementos a la fila
for i in range(n):
    print ('Estado actual de la fila')
    queue.printList()
    queue.enqueue(i+1)
    print('------------------------------')
#Eliminar elementos de la fila
for i in range(n+1):
    if queue.getLen()!=0:
        print ('Estado actual de la fila')
        queue.printList()
        print('------------------------------')
        print ('Sale de la fila:',end=' ')
        print ('('+str(queue.dequeue().getData())+')')
        print()
    else:
        print ('Estado actual de la fila')
        queue.printList()
        print('------------------------------')


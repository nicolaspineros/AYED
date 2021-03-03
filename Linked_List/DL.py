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


# Doubly Linked List definition
class MyDoublylinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insertHead(self, item):

        #Insert Head
        newnode = Node(item)
        newnode.setNext(self.head)
        newnode.setPrev(None)

        if self.head is not None:
            self.head.setPrev(newnode)

        self.head = newnode
        self.len += 1

    def insertTail(self, item):
        newnode = Node(item)
        self.tail = self.head
        newnode.setNext(None)
        #Insert After Tail
        if self.head == None and self.tail == None:
            newnode.setPrev(None)
            self.head, self.tail = newnode, newnode
            return

        while self.tail.getNext() is not None:
            self.tail = self.tail.getNext()

        self.tail.setNext(newnode)
        newnode.setPrev(self.tail)

        self.len += 1

    def insertAtMid(self,item):
        # if list is empty
        if self.head is None:
            self.head = Node(item)

        else:

            # get a new node
            newnode = Node(item)

            # assign values to the pre and aft pointers
            pre = self.head
            aft = self.head.getNext()

            while aft != None and aft.getNext() != None:
                # move pre pointer to next node
                pre = pre.getNext()

                # move aft pointer two nodes at a time
                aft = aft.getNext().getNext()

            # insert the 'newnode' and adjust the required links
            newnode.setNext(pre.getNext())
            pre.getNext().setPrev(newnode)
            pre.setNext(newnode)
            newnode.setPrev(pre)

        self.len += 1


    def insertAtIndex(self,index,item):
        #Specific Insertion
        prenode = self.head

        for i in range(index-1):
            prenode = prenode.getNext()

        aftnode = prenode.getNext()
        newnode = Node(item)
        newnode.setNext(aftnode)
        aftnode.setPrev(newnode)
        prenode.setNext(newnode)
        newnode.setPrev(prenode)

        self.len += 1

    def removeHead(self):
        if self.len == 0:
            return
        else:
            prenode = self.head
            # Toma el siguiente como la nueva Cabeza
            self.head = prenode.getNext()
            # Eliminar relacion innecesaria
            if self.head is None:
                self.tail = None

            prenode.setNext(None)

            if self.head is not None:
                self.head.setPrev(None)

            self.len -= 1

    def removeTail(self):
        if self.len == 0:
            return
        else:
            prenode = self.tail
            prenode.setPrev(self.tail)
            prenode.setNext(None)

            self.len -= 1

    def removeAtIndex(self, index):
        if self.len == 0:
            return
        else:
            # Specific deleting
            prenode = self.head

            for i in range(index - 1):
                prenode = prenode.getNext()

            delete = prenode.getNext()
            aftnode = delete.getNext()
            prenode.setNext(aftnode)
            aftnode.setPrev(prenode)
            delete.setNext(None)

            self.len -= 1

    def removeItem(self, item):
        try:
            itemnode = self.head
            prenode = None
            found = False

            while itemnode.getData() != item:
                prenode = itemnode
                itemnode = itemnode.getNext()

            if prenode == None:
                self.head = itemnode.getNext()
            else:
                prenode.setNext(itemnode.getNext())
                itemnode.getNext().setPrev(prenode)

        except:
            return -1

    def search(self, item):
        if self.len == 0:
            return 'No encontrado'
        else:
            index = 0
            prenode = self.head
            while prenode.getData() != item:
                index +=1
                prenode = prenode.getNext()

                if prenode is None:
                    return 'No encontrado'

            return 'Encontrado, en el indice: '+str(index)


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

#Creando lista inicial
linkedlist = MyDoublylinkedList()
for i in range(5):
    linkedlist.insertTail(i+1)

#Seleccionando operacion a realizar
print()
print('----------------------------------------------')
print('             DOUBLY LINKED LIST')
print('----------------------------------------------')
print('----------------------------------------------')
print('Tiene 3 opciones, dada una lista [1,2,3,4,5]')
print('1.Insertar')
print('2.Remover')
print('3.Buscar')
print('4.Conocer estado de la lista')
print('5.Salir')
print()
print('Que desea hacer:')
n=int(stdin.readline().strip())
print('----------------------------------------------')
while n!=5:
    #Insertar un elemento
    if n==1:
        print('--------------------------------')
        print('             INSERT')
        print('--------------------------------')
        print('--------------------------------')
        print('1.Insertar en la cabeza')
        print('2.Insertar en la cola')
        print('3.Insertar en la mitad')
        print('4.Insertar dado un indice')
        print('5.Otra operacion')
        print()
        print('Que desea hacer:')
        n = int(stdin.readline().strip())
        print('--------------------------------')
        while n!=5:
            if n==1:
                print('Insertar en la Cabeza:')
                num = int(stdin.readline().strip())
                while linkedlist.search(num)!='No encontrado':
                    print('No esta permitido numeros repetidos.')
                    print('Insertar numero nuevamente:')
                    num = int(stdin.readline().strip())
                linkedlist.insertHead(num)
            elif n==2:
                print('Insertar en la Cola:')
                num = int(stdin.readline().strip())
                while linkedlist.search(num) != 'No encontrado':
                    print('No esta permitido numeros repetidos.')
                    print('Insertar numero nuevamente:')
                    num = int(stdin.readline().strip())
                linkedlist.insertTail(num)
            elif n==3:
                print('Insertar en la Mitad:')
                num = int(stdin.readline().strip())
                while linkedlist.search(num) != 'No encontrado':
                    print('No esta permitido numeros repetidos.')
                    print('Insertar numero nuevamente:')
                    num = int(stdin.readline().strip())
                linkedlist.insertAtMid(num)
            elif n==4:
                print('Insertar numero:')
                num = int(stdin.readline().strip())
                print('En el indice:')
                i = int(stdin.readline().strip())
                while linkedlist.search(num) != 'No encontrado':
                    print()
                    print('No esta permitido numeros repetidos.')
                    print('Insertar numero nuevamente:')
                    num = int(stdin.readline().strip())
                    print('En el indice:')
                    i = int(stdin.readline().strip())
                linkedlist.insertAtIndex(i,num)
            else:
                print('------------------------------------')
                print(' Elige nuevamente. No es una opcion')
                print('------------------------------------')
            #Visualizando insercion
            print('-----------------------------')
            print('  Estado actual de la lista')
            print()
            linkedlist.printList()
            print('-----------------------------')

            #Nuevamente insertando
            print('--------------------------------')
            print('             INSERT')
            print('--------------------------------')
            print('--------------------------------')
            print('1.Insertar en la cabeza')
            print('2.Insertar en la cola')
            print('3.Insertar en la mitad')
            print('4.Insertar dado un indice')
            print('5.Otra operacion')
            print()
            print('Que desea hacer:')
            n = int(stdin.readline().strip())
            print('--------------------------------')

    #Remover un elemento
    elif n==2:
        print('--------------------------------')
        print('             REMOVE')
        print('--------------------------------')
        print('--------------------------------')
        print('1.Remover la cabeza')
        print('2.Remover la cola')
        print('3.Remover dado un indice')
        print('4.Remover un elemento')
        print('5.Otra operacion')
        print()
        print('Que desea hacer:')
        n = int(stdin.readline().strip())
        print('--------------------------------')

        while n != 5:
            if n == 1:
                linkedlist.removeHead()
            elif n == 2:
                linkedlist.removeTail()
            elif n == 3:
                print('Remover el indice:')
                i = int(stdin.readline().strip())
                while i > linkedlist.len or i==0 or i==linkedlist.len:
                    if i > linkedlist.len:
                        print('El indice excede la longitud de la lista actual.')
                    else:
                        print('Ingrese in indice entre [1..'+str(linkedlist.len-1)+']')
                    print('Ingresar el indice nuevamente:')
                    i = int(stdin.readline().strip())
                linkedlist.removeAtIndex(i)
            elif n == 4:
                print('Remover el numero:')
                num = int(stdin.readline().strip())
                while linkedlist.search(num) == 'No encontrado':
                    print('El numero no se encuentra en la lista.')
                    print('Ingresar nuevamente')
                    num = int(stdin.readline().strip())
                    print('--------------------------------------')
                linkedlist.removeItem(num)
            else:
                print('------------------------------------')
                print(' Elige nuevamente. No es una opcion')
                print('------------------------------------')
            # Visualizando eliminacion
            print('-----------------------------')
            print('  Estado actual de la lista')
            print()
            linkedlist.printList()
            print('-----------------------------')

            # Nuevamente eliminando
            print('--------------------------------')
            print('             REMOVE')
            print('--------------------------------')
            print('--------------------------------')
            print('1.Remover la cabeza')
            print('2.Remover la cola')
            print('3.Remover dado un indice')
            print('4.Remover un elemento')
            print('5.Otra operacion')
            print()
            print('Que desea hacer:')
            n = int(stdin.readline().strip())
            print('--------------------------------')
    #Buscar elemento
    elif n == 3:
        print('-----------------------------------')
        print('             SEARCH')
        print('-----------------------------------')
        print('Ingrese el numero que desea buscar:')
        num = int(stdin.readline().strip())
        print()
        print(linkedlist.search(num))
        print('-----------------------------------')
    elif n==4:
        #Visualizando lista
        print('-----------------------------')
        print('  Estado actual de la lista')
        print()
        linkedlist.printList()
        print('-----------------------------')
    else:
        print('------------------------------------')
        print(' Elige nuevamente. No es una opcion')
        print('------------------------------------')

    #Seleccionando operacion
    print()
    print('----------------------------------------------')
    print('             DOUBLY LINKED LIST')
    print('----------------------------------------------')
    print('----------------------------------------------')
    print('Tiene 3 opciones, dada una lista [1,2,3,4,5]')
    print('1.Insertar')
    print('2.Remover')
    print('3.Buscar')
    print('4.Conocer estado de la lista')
    print('5.Salir')
    print()
    print('Que desea hacer:')
    n = int(stdin.readline().strip())
    print('----------------------------------------------')

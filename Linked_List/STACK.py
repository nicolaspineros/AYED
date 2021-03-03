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

# Stack definition
class Mystack:

    def __init__(self):
        self.head = None
        self.len = 0

    def push(self,item):
        newnode = Node(item)
        newnode.setNext(self.head)
        self.head = newnode
        self.len += 1

    def pop(self):
        newnode = self.head
        self.head = newnode.getNext()
        newnode.setNext(None)
        self.len -= 1

    def getLen(self):
        return self.len

    def peek(self):
        return self.head.getData()

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

stack = Mystack()
n=int(stdin.readline().strip())
#Ingresar elementos a la pila
for i in range(n):
    print ('Estado actual de la pila')
    stack.printList()
    stack.push(i+1)
    print('------------------------------')

#Eliminar elementos de la pila
for i in range(n+1):
    if stack.getLen()!=0:
        print ('Estado actual de la pila')
        stack.printList()
        print('------------------------------')
        print ('Sale de la pila:',end=' ')
        print ('('+str(stack.peek())+')')
        stack.pop()
        print()
    else:
        print ('Estado actual de la pila')
        stack.printList()
        print('------------------------------')

  

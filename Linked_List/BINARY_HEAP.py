from sys import stdin
class Heap(object):

    def __init__(self):
        self.array = []
        self.lastIndex = -1

    def parent(self, index):
        return (( index // 2 ) - 1) if index % 2 == 0 else ( index // 2 )

    def leftChild(self, index):
        return (index * 2) + 1

    def rightChild(self, index):
        return 2*(index + 1)

    #Insertar un nodo, i es el ultimo indice del array
    def insert(self, item):
        self.array.append(item)
        self.lastIndex +=1
        self.shiftUp(self.lastIndex)

    def shiftUp(self,index):

        newnode = self.array[index]
        if index > 0 and self.compare(newnode, self.array[self.parent(index)]):
            self.array[self.parent(index)], self.array[index] = newnode, self.array[self.parent(index)]
            self.shiftUp(self.parent(index))
        return

    def shiftDown(self,index):
        newnode = self.array[index]
        #No tiene hijos
        if self.rightChild(index) > len(self.array) and self.leftChild(index) > len(self.array):
            return

        else:
            #Tiene dos hijos
            if self.rightChild(index) < len(self.array) and self.compare(self.array[self.rightChild(index)], self.array[self.leftChild(index)])  and self.leftChild(index) < len(self.array):
                if self.array[self.rightChild(index)] > self.array[self.leftChild(index)]:
                    maxChild = self.rightChild(index)
                else:
                    maxChild = self.leftChild(index)

            #Tiene solo uno
            elif self.leftChild(index) < len(self.array):
                maxChild = self.leftChild(index)
            else:
                maxChild = self.rightChild(index)

            #Swap
            self.array[index], self.array[maxChild] = self.array[maxChild], newnode
            self.shiftDown(maxChild)
        return

    def compare(self,node,node1):
        raise NotImplementedError

    #Remover el Maxnodo
    def extractMax(self):

        if self.lastIndex == -1:
            raise IndexError("Can't pop from empty heap")
        newnode = self.array[0]
        if self.lastIndex > 0: # more than one element in the heap
            self.array[0] = self.array[self.lastIndex]
            self.shiftDown(0)

        #Reducir el array
        self.lastIndex -=1
        self.array = self.array[:-1]

        return newnode

    def heapSort(self):
        for i in range(self.lastIndex):
            self.extractMax()
            self.printer()

    def peek(self):
        if not self.array:
            return None
        return self.array[0]

    def printer(self):
        print(self.array)

class minHeap(Heap):
    def compare(self,node,node1):
        return node < node1

class maxHeap(Heap):
    def compare(self,node,node1):
        return node > node1


def main():
    print ('MinHeap O(N log N):', end = ' ')
    myHeap = minHeap()
    #lst = [x for x in range(31)]
    #for i in lst:
    #    myHeap.insert(i)
    myHeap.insert(33)
    myHeap.insert(60)
    myHeap.insert(5)
    myHeap.insert(15)
    myHeap.insert(25)
    myHeap.insert(12)
    myHeap.insert(45)
    myHeap.insert(70)
    myHeap.insert(35)
    myHeap.insert(7)
    myHeap.printer()
    #print ('La raiz del arbol es:')
    #print (myHeap.peek())
    #print ('Luego de remover el Min:')
    #myHeap.extractMax()
    #myHeap.printer()
    print()
    print ('MaxHeap O(N log N):', end = ' ')
    myHeap = maxHeap()
    lst = [x for x in range(10)]
    for i in lst:
        myHeap.insert(i)
    #myHeap.insert(2)
    #myHeap.insert(7)
    #myHeap.insert(3)
    #myHeap.insert(1)
    #myHeap.insert(9)
    #myHeap.insert(44)
    #myHeap.insert(23)
    myHeap.printer()
    print ()
    #print ('La raiz del arbol es:')
    #print (myHeap.peek())
    print ('Luego de remover el Max:',end=' ')
    myHeap.extractMax()
    myHeap.printer()
    #print ('-------------------------------')

main()
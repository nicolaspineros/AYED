"""Programa para determinar el numero minimo
de swaps necesarios para ordenar la entrada dada"""

from sys import stdin

def merge_sort(num):
    global cont
    cont = 0
    if len(num) <= 1:
        return num
    L = []
    R = []
    mid = len(num)// 2
    for i in range(0,mid):
        L.append(num[i])
    for i in range(mid,len(num)):
        R.append(num[i])
    #print(L)   para ver el proceso de las listas con el merge  
    #print(R)
    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L,R)

def merge(L,R):
    global cont
    arreglo = []
    i = 0
    j = 0
    while (i < len(L) and j < len(R)):
        if (L[i] <= R[j]):
            arreglo.append(L[i])
            i = i + 1
            cont = cont + 1
        else:
            arreglo.append(R[j])
            j = j + 1
            cont = cont + 1
    while (i < len(L)):
        arreglo.append(L[i])
        i = i + 1
    while (j < len(R)):
        arreglo.append(R[j])
        j = j + 1

    return arreglo

def main():
    """Creamos la lista num donde vamos a hacer nuestro arreglo """
    num = []
    """La primera linea del input es el caso que es la longitud de la secuencia"""
    caso = int(input(""))
    """Nuestro programa termina cuando el caso/longitud es igual a cero"""
    while caso != 0:
        for i in range(0,caso):
            n = int(stdin.readline())
            num.append(n)
        """Despues de crear nuestra secuencia y colocarla en el arreglo vamos a usar 
        el algoritmo de ordenamiento merge sort"""
        num = merge_sort(num)
        print(num)
        num = []
        print(cont)
        caso = int(input(" "))

main()
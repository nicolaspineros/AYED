# Train Swapping
# Nicolas Piñeros Campo

from sys import stdin

def insertion_sort(tren,vagones):
    """definimos la funcion para hacer el ordenamiento
     tren = nuestra lista para arreglar, vagones = numero de vagones que determina la longitud
     tenemos un contador = 0 para determinar cuantos cambios se hacen en el ordenamiento"""
    contador = 0
    for j in range(1, vagones):
        llave = tren[j]
        i = j - 1
        while i >= 0:
            if llave < tren[i]:
                tren[i + 1] = tren[i]
                tren[i] = llave
                i = i - 1
                contador = contador + 1
            else:
                break
    return contador

def main():
    """Nuestra primera entrada es el numero de casos que vamos a procesar"""
    casos = int(input())
    for i in range(0,casos):
        vagones = int(input())
        tren = stdin.readline().strip().split(" ")
        """Ya teniendo nuestra lista hacemmos el llamado de la funcion mediante la variable ordenar"""
        ordenar = insertion_sort(tren,vagones)
        """una vez ordenada la lista o tren mostramos la cantidad de cambios realizados""" 
        print(ordenar)
main()


"""Programa dado un camino (cad), una posicion(x) y una velocidad inicial (vel)
 indica si es posible detenerse a lo largo del camino sin pisar ningun clavo"""

from sys import stdin

def rec(cad,vel,x):
    if (vel,x) in dic:
        return dic[(vel,x)]
    else:
        """casos base"""
        if (x >= len(cad)+1):
            return False
        elif (vel == 0 and cad[x] == "T"):
            return True
        elif (cad[x]=="F"):
            return False
        else:
            """caso de incremento o decremento en la velocidad"""
            dic[(vel,x)] = (rec(cad,vel,x+vel) or rec(cad,vel-1,x+vel) or rec(cad,vel+1,x+vel))
            return dic[(vel,x)]

def main():

    cad = ["T","F","T","T","T","F","T","T","F","T","T"]
    """Los clavos son representados por F"""
    global dic
    dic = dict()
    print(cad)
    """vel es la velocidad inicial, x es la posicion inicial y rec la funcion recursiva """
    vel = int(stdin.readline())
    x = int(stdin.readline())
    print(rec(cad,vel,x))

main()
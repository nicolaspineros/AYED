
"""Este programa calcula cuantas maneras diferentes existen que 8 reinas esten en el tablero sin matarse"""
pos = ['']*8,
def reinas(c):
    global pos#Lista global
    if c == 8:# si c esta en la ultima posicion de la lista quiere decir que encontro una manera de poner las 8 reinas sin matarse
        #print(pos)    Todas las posibles maneras que existen :)
        return 1  # retorna una posibilidad
    s = 0   #contador
    for f in range(8):#Esto es lo escencial del backtraking, el ciclo les ayudara a recorrer todas las maneras posibles que puede estar el tablero
        pos[c] = f # coloca una ficha de prueba
        if not se_atacan(c):
            s+=reinas(c+1) #Encontro que en esa posicion no esta siendo atacado, pase a la siquiente posicion de la lista
    return s #retorna el objetivo
def se_atacan(c):
    global pos 
    for i in range(c): #revisa hasta la posicion de la lista en la que este
        if pos[i] == pos[c] or i+pos[i] == c+pos[c] or i-pos[i] == c-pos[c]:#Revisa si no esta a laterales o diagonales otra reina
            # dos reinas en la misma fila o en la misma columna
            return True
    return False
print(reinas(0))
#Es un buen codigo base... :)... Con que entiendan como recorre este codigo, ya backtraking sera papas
def main():
  a=int(sys.stdin.readline().strip())
  lista=[]
  for i in range(a):
      b=[sys.stdin.readline().strip()]
      lista.append(b)




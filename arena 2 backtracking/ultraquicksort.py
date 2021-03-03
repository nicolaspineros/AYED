import sys
def ultrasort(lista):
    cont=0
    if len (lista)>1:
        izq,der=dividiralmedio(lista)
        cont+=ultrasort(izq)
        cont+=ultrasort(der)
        i,j,k=0,0,0
        while i < len(izq) and j < len(der):
            if izq[i]<der[j]:
                lista[k]=izq[i]
                i+=1
            else:
                lista[k]=der[j]
                j+=1
                cont+=len(izq)-i
            k+=1
        while j <len(der):
            lista[k]=der[j]
            j+=1
            k+=1
        while i <len(izq):
            lista[k]=izq[i]
            i+=1
            k+=1
    return cont
def dividiralmedio(lista):
    middle=len(lista)//2
    return lista [0:middle], lista[middle:]
def main():
  a=int(sys.stdin.readline().strip())
  while a!=0:
    z=[]
    for i in range(a):
      b=int(sys.stdin.readline().strip())
      z.append(b)
    print(ultrasort(z))
    a=int(sys.stdin.readline().strip())
    
main()

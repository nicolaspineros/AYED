
from sys import stdin

from string import ascii_uppercase

def convertir_base(secuencia,ls):
    AUX = []

    for i in range(len(secuencia)):

        for j in range(len(ascii_uppercase)):
            """print(j)"""
            if secuencia[i] == ascii_uppercase[j]:
                n = j
                AUX.append(n)
    print(ls)
    print(AUX)
    return AUX

def base(secuencia,lnum):

    acum = 0
    for i in range(len(lnum)):
        acum = acum + lnum[i]
    print("La palabra " + str(secuencia) + "en base 36 es: " + str(acum))
    return acum

def main():

    NUM = [0,1,2,3,4,5,6,7,8,9]
    secuencia = stdin.readline()
    ls = list(ascii_uppercase) + NUM
    lnum = convertir_base(secuencia,ls)
    base(secuencia,lnum)

main()
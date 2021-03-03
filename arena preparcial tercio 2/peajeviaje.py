from sys import stdin


def viaje(n,t,a):
    global peajes,diccionario
    if n<=0:
        return 0
    if (n,t,a) not in diccionario:
        if a==0 or t==0:
            if a==0 and t==0:
                diccionario[(n,t,a)] = sum(peajes[0:n])
            elif t==0 :
                diccionario[(n, t, a)] = min(viaje(n-5,t,a-1),peajes[n-1]+viaje(n-1,t,a))
            elif a==0 :
                diccionario[(n, t, a)] = min(viaje(n-3,t-1,a),peajes[n-1]+viaje(n-1,t,a))
        else:
            diccionario[(n, t, a)] = min(viaje(n-3,t-1,a),viaje(n-5,t,a-1),peajes[n-1]+viaje(n-1,t,a))

    return diccionario[(n,t,a)]

def main():
    global peajes,diccionario
    casos=int(stdin.readline())
    for i in range(casos):
        diccionario={}
        n,t,a=list(map(int,stdin.readline().strip().split()))
        peajes=list(map(int,stdin.readline().strip().split()))
        print(viaje(n,t,a))
main()



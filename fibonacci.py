#Algoritmo serie de fibonacci

def main():
    print("Bievenidos a nuestro Sistema")
    n = int(input("Diga la cantidad de numeros: "))
    n1 = 0
    n2 = 1
    if n <= 0:
        print("n debe ser mayor a 0")
    else:
        for i in range(0,n-1):
            if i == 0:
                print(i)
            if i == 1:
                print(i)
            else:
                resp = n1 + n2
                print(resp)
                n1 = n2
                n2 = resp
main()


from sys import stdin
def main():
    num=int(stdin.readline().strip())
    print(bina(num))
def bina(n):
    if n==2 or n==3:
        return str(n%2)+str(n//2)
    else:
        b=n%2
        c=n//2
        return str(b) + str(bina(c))
        
main()

'''
Casos Prueba:
INPUT:
77
OUTPUT:
1011001

INPUT:
28
OUTPUT:
00111

'''

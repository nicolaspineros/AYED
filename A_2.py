from sys import stdin

def main():
    
    n = list(map(int,stdin.readline().split()))
    numeros={}
    for i in (n):
        if i not in numeros:
            numeros[i]=1
        else:
            numeros[i]+=1

    for j in (numeros):
        print(j,numeros[j])
        
main()

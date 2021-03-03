from sys import stdin

def merge_sort(num):
    if len(num) <= 1:
        return num
    L = []
    R = []
    mid = len(num)// 2
    for i in range(0,mid):
        L.append(num[i])
    for i in range(mid,len(num)):
        R.append(num[i])
    print(L)
    print(R)
    L = merge_sort(L)
    R = merge_sort(R)

    return merge(L,R)

def merge(L,R):
    arreglo = []
    i = 0
    j = 0
    while (i < len(L) and j < len(R)):
        if (L[i] <= R[j]):
            arreglo.append(L[i])
            i = i + 1
        else:
            arreglo.append(R[j])
            j = j + 1
    while (i < len(L)):
        arreglo.append(L[i])
        i = i + 1
    while (j < len(R)):
        arreglo.append(R[j])
        j = j + 1

    return arreglo

def main():
    num = []
    caso = int(input("caso: "))
    while caso != 0:
        for i in range(0,caso):
            n = int(stdin.readline())
            num.append(n)
        num = merge_sort(num)
        print(num)
        num = []
        caso = int(input("caso: "))
    """num =[6,5,3,1,8,7,2,4]
    print(num)
    num = merge_sort(num)
    print(num)"""

main()
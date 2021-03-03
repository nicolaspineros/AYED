from sys import stdin

#tren = stdin.readline().strip().split(" ")


def insertion_sort(list):
    for j in range(1, len(list)):
        llave = list[j]
        i = j - 1
        while i > 0:
            if llave < list[i]:
                list[i + 1] = list[i]
                list[i] = llave
                i = i - 1
            else:
                break

a = insertion_sort([2,1,4,3])
print(a)

